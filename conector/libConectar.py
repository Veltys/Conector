#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    libConectar

    @file       : libConectar.py
    @brief      : Server connection library

    @author     : Veltys
    @date       : 2023-04-20
    @version    : 3.2.0
    @usage      : import libConectar | from libConectar import ...
    @note       : ...
'''


from ansible.inventory.manager import InventoryManager                          # Ansible inventory manager
from ansible.parsing.dataloader import DataLoader                               # Ansible data loader
from ansible.parsing.vault import VaultSecret                                   # Ansible vault parser
from ansible.vars.manager import VariableManager                                # Ansible vars manager
from exitstatus import ExitStatus                                               # Exit codes
import argparse                                                                 # Argument processor functions
import os                                                                       # Miscellaneous operating system interfaces
import sys                                                                      # System-specific parameters and functions

from .config import *                                                           # Config file


class libConectar:
    _ansible_vault_pass = None
    _args = None
    _changeConsoleTitle = None
    _ssh_key = None
    _command = None
    _default_ansible_user = None
    _host_vars = None
    _inventory_dir_names = None
    _vault_pass_file = None

    def __init__(
            self,
            argv = None,
            changeConsoleTitle = False,
            ssh_key = SSH_KEY,                                                  # @UndefinedVariable
            command = '',
            default_ansible_user = DEFAULT_ANSIBLE_USER,                        # @UndefinedVariable
            inventory_dir_names = INVENTORY_DIR_NAMES,                          # @UndefinedVariable
            vault_pass_file = VAULT_PASS_FILE                                   # @UndefinedVariable
        ):
        '''!
            Class constructor
            
            Initializes default values of the class
        '''

        self._ssh_key = ssh_key
        self._changeConsoleTitle = changeConsoleTitle
        self._command = command
        self._default_ansible_user = default_ansible_user
        self._inventory_dir_names = inventory_dir_names
        self._vault_pass_file = vault_pass_file

        if argv != None:
            self._args = self.parseClArgs(argv)


    def _executeCommand(self, command = None, changeConsoleTitle = None, host = None):
        '''!
            Runs the given command

            @param command              : Command
            @param changeConsoleTitle   : Change console title

            @return                     : Command output
        '''

        if command == None:
            command = self._command

        if command == 'conectar':
            user = self._host_vars.get('ansible_user') if self._host_vars.get('ansible_user') != None else self._default_ansible_user

            if host == None:
                host = self._host_vars.get('ansible_host')

            if changeConsoleTitle:
                self._doChangeConsoleTitle(f"\033]30;(" + user + f") { self._host_vars.get('ansible_host') }\007")

            print(f"Connecting to { host } ➡️ { user }@{ self._host_vars.get('ansible_host') }:{ self._host_vars.get('ansible_port') }..." + ' ') # Damn emojis 😢
            res = os.system(f"ssh -i { self._ssh_key } " + (f"-L { self._args.local_bind }" if self._args.local_bind is not None else '') + f" -p { self._host_vars.get('ansible_port') } '" + user + f"@{ self._host_vars.get('ansible_host') }'")

            if changeConsoleTitle:
                self._doChangeConsoleTitle("\033]30;%d : %n")                   # Restores the original console title

            return res

        elif command == 'montar':
            user = (self._host_vars.get('ansible_user') if self._host_vars.get('ansible_user') != None else self._default_ansible_user)

            os.makedirs(f"/media/servidores/{ self._host_vars.get('host_id') }/", exist_ok = True)
            if os.system(f"sudo sshfs { user }@{ self._host_vars.get('ansible_host') }:/home/{ user } /media/servidores/{ self._host_vars.get('host_id') }/ -o allow_other,default_permissions,uid=1001,gid=1001,IdentityFile={ self._ssh_key } -p { self._host_vars.get('ansible_port') }") == ExitStatus.success:
                return f"El servidor <{ self._host_vars.get('host_id') }> se ha montado correctamente"
            else:
                return f"No ha sido posible montar correctamente el servidor <{ self._host_vars.get('host_id') }>"
        elif command == 'desmontar':
            if os.system("sudo umount " + ('-l' if self._args.lazy else '') + f" /media/servidores/{ self._host_vars.get('host_id') }/") == ExitStatus.success:
                os.rmdir(f"/media/servidores/{ self._host_vars.get('host_id') }/")

                return f"El servidor <{ self._host_vars.get('host_id') }> se ha desmontado correctamente"
            else:
                return f"No ha sido posible desmontar correctamente el servidor <{ self._host_vars.get('host_id') }>"
        else:
            print(f"El comando <{ command }> es incorrecto", file = sys.stderr)

            return ExitStatus.failure


    @staticmethod
    def _doChangeConsoleTitle(title):
        '''!
            Changes the original console title

            @param title                : Console title
        '''

        sys.stdout.write(title)
        sys.stdout.flush()


    def parseClArgs(self, argv):
        '''!
            Processes the arguments passed to the program

            @param argv                 : Arguments vector

            @return                     : Processed arguments
        '''

        parser = argparse.ArgumentParser()
        parser.add_argument('server', nargs = '?', help = 'Servidor al que se quiere conectar', type = str)
        parser.add_argument('-c', '--completion', action = 'store_true', help = 'Modo de autocompletar')

        if self._command == 'conectar':
            parser.add_argument('-L', action = 'store', dest = 'local_bind', help = 'Pasa directamente al cliente SSH el contenido de esta opción con el parámetro \'-L\' (ver \'man ssh\' para más detalles)')
        elif self._command == 'desmontar':
            parser.add_argument('-l', '--lazy', action = 'store_true', help = 'desvincula el sistema de ficheros ahora y limpia más tarde', required = False)

        args = parser.parse_args(argv)

        return args


    def run(self, command = None, changeConsoleTitle = None):
        '''!
            Class runner

            Performs the necessary pre-tasks and runs the provided command

            @param command              : Command to run
            @param changeConsoleTitle   : Change console title
        '''

        if command == None:
            command = self._command

        if changeConsoleTitle == None:
            changeConsoleTitle = self._changeConsoleTitle

        if self._args == None:
            return False
        else:
            loader = DataLoader()

            if os.path.exists(self._vault_pass_file):
                try:
                    f = open(self._vault_pass_file, 'r')
                except IOError:
                    pass
                else:
                    self._ansible_vault_pass = f.read()

                    loader.set_vault_secrets([('default', VaultSecret(_bytes = str.encode(self._ansible_vault_pass)))])

                    f.close()

            inventories = []
            variable_managers = []

            for inventory_dir_name in self._inventory_dir_names:
                inventories.append(InventoryManager(
                    loader = loader,
                    sources = [
                        os.path.join(inventory_dir_name, filename) \
                        for filename \
                        in os.listdir(inventory_dir_name) \
                        if os.path.isfile(os.path.join(inventory_dir_name, filename))
                    ]
                ))

            for inventory in inventories:
                variable_managers.append(VariableManager(loader = loader, inventory = inventory))

            res = ''

            for i, _ in enumerate(inventories):
                if \
                    len(vars(self._args)) == 0 or \
                    (\
                        self._args.server == None and \
                        self._args.completion == False
                    ):
                    self.parseClArgs(['-h'])
                elif self._args.completion:
                    for h in inventories[i].hosts:
                        res += f"{ h } "

                    for g in inventories[i].groups:
                        res += f"{ g } "

                    res += "\n"
                elif self._args.server in inventories[i].get_groups_dict()['all']:
                    host = inventories[i].get_host(self._args.server)

                    self._host_vars = variable_managers[i].get_vars(host = host)

                    res = self._executeCommand(command, changeConsoleTitle, host)

                    return res
                elif self._args.server in inventories[i].get_groups_dict():
                    res = 0

                    for host in inventories[i].get_groups_dict()[self._args.server]:
                        host = inventories[i].get_host(host)

                        self._host_vars = variable_managers[i].get_vars(host = host)

                        res = res + self._executeCommand(command, changeConsoleTitle, host)

                    return res
                else:
                    res = False

            if not res:
                print(f"ERROR: El servidor <{ self._args.server }> no existe", file = sys.stderr)

            return res
