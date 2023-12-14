#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    install_script

    @file       : install_script.py
    @brief      : Custom installer

    @author     : Veltys
    @date       : 2023-03-21
    @version    : 1.0.0
    @usage      : (imported by setup.py)
    @note       : ...
'''


from distutils.command.install import install                                   # Building and installing Python modules
import os                                                                       # Miscellaneous operating system interfaces
import platform                                                                 # Access to underlying platform’s identifying data
import shutil                                                                   # High-level file operations


class InstallationError(Exception):
    '''!
        Custom exception for installation errors
    '''

    def __init__(self, message):
        '''!
            Class constructor
            
            Initializes default values of the class
        '''

        self.message = message
        super().__init__(self.message)


class CustomInstall(install):
    '''!
        CustomInstall is a subclass of the setuptools 'install' command

        This class provides a custom installation process for the 'conector'
        package, handling the installation of Bash completion files and aliases
        on Linux systems
    '''

    def run(self):
        '''!
            Executes the custom installation process

            This method first checks if the current platform is Linux, and if so,
            copies the appropriate Bash completion files and aliases to their
            respective system locations

            Then, it proceeds with the normal installation process
        '''

        if platform.system() != 'Linux':
            print(f"Unfortunately, autocompletion function is not yet supported on your operating system ({ platform.system() }).")
            print('The installation process are going to continue without this funcion. Sorry for the inconveniences.')

        try:
            if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'conector/config.py')):
                if os.geteuid() == 0:
                    src_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bash_completion')

                    dst_path = '/etc/bash_completion.d'

                    for file in os.listdir(src_path):
                        if file.endswith("-completion.bash"):                   # Copy Bash autocompletion files to /etc/bash_completion.d/
                            src_file = os.path.join(src_path, file)
                            dst_file = os.path.join(dst_path, file)

                            shutil.copy2(src_file, dst_file)

                        print(f"Copied {src_file} to {dst_file}")

                else:
                    raise InstallationError('Error: This script must be run with superuser permissions on Linux systems')

            else:
                raise InstallationError('Error: Please, read \'Configuration\' section in README.md file before executing installation')

        except InstallationError as e:
            print(e.message)
            print('The installation process cannot continue')

        else:
            install.run(self)                                                   # Run normal installation
