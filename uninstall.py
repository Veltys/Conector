#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    install_script

    @file       : install_script.py
    @brief      : Custom installer

    @author     : Veltys
    @date       : 2023-11-04
    @version    : 1.0.1
    @usage      : (imported by setup.py)
    @note       : ...
'''


import os                                                                       # Miscellaneous operating system interfaces
import platform                                                                 # Access to underlying platform’s identifying data
import subprocess                                                               # Subprocess management
import sys                                                                      # System-specific parameters and functions


def remove_bash_completion_files():
    '''!
        Removes the Bash completion files for the 'conector' package

        This function iterates through the files in ./bash_completion/
        and removes the corresponding files which are related to the
        'conector' package from their installed path
    '''


    if platform.system() == 'Linux':
        src_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bash_completion')
        dst_paths = {
            'aliases': '/etc/profile.d/',
            'bash': '/etc/bash_completion.d',
        }

        for file in os.listdir(src_path):
            if file.endswith("-completion.bash"):
                system_file_path = os.path.join(dst_paths['bash'], file)

            try:
                os.remove(system_file_path)

                print(f"Removed {system_file_path}")

            except Exception as e:
                print(f"Error removing {system_file_path}: {str(e)}")


def uninstall_package(package_name):
    '''!
        Uninstalls the specified Python package using pip

        @param package_name:    The name of the package to uninstall

        This function uninstalls the given Python package using pip
        and prints a message to inform the user about the status of the
        uninstallation process
    '''


    try:
        subprocess.run(['pip', 'uninstall', '-y', package_name], check = True)

        print(f"Uninstalled {package_name}")

    except Exception as e:
        print(f"Error uninstalling {package_name}: {str(e)}")


def main(argv):
    '''!
        Performs the needed operations to uninstall the package

        @param argv:            Program arguments

        @return:                Return code
    '''


    remove_bash_completion_files()
    uninstall_package('conector')


if __name__ == "__main__":
    main(sys.argv[1:])
