#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    Montar

    @file       : montar.py
    @brief      : fuse.sshfs mounting system for servers' home directory

    @author     : Veltys
    @date       : 2023-03-17
    @version    : 2.0.1
    @usage      : python montar.py -s server_or_group | python3 montar.py -s server_or_group | ./montar.py -s server_or_group
    @note       : ...
'''


from conector.libConectar import libConectar                                    # Connection library
from exitstatus import ExitStatus                                               # POSIX exit status codes
import sys                                                                      # System-specific parameters and functions


def main(argv = sys.argv[1:]):
    '''!
        Performs the needed operations to mount

        @param argv:    Program arguments

        @return:        Return code
    '''


    conector = libConectar(argv, command = 'montar')

    res = conector.run()

    if type(res) == str:
        print(res)
    elif type(res) == bool:
        if res:
            sys.exit(ExitStatus.success)
        else:
            sys.exit(ExitStatus.failure)
    elif type(res) == ExitStatus:
        sys.exit(res)
    else:
        sys.exit(ExitStatus.failure)


if __name__ == "__main__":
    main(sys.argv[1:])
