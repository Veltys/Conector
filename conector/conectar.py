#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    Conectar

    @file       : conectar.py
    @brief      : Server connection system

    @author     : Veltys
    @date       : 2023-11-04
    @version    : 2.0.2
    @usage      : python conectar.py -s server_or_group | python3 conectar.py -s server_or_group | ./conectar.py -s server_or_group
    @note       : ...
'''


import sys                                                                      # System-specific parameters and functions

from exitstatus import ExitStatus                                               # POSIX exit status codes

from conector.libConectar import libConectar                                    # Connection library


def main(argv = sys.argv[1:]):
    '''!
        Performs the needed operations to connect

        @param argv:    Program arguments

        @return:        Return code
    '''


    conector = libConectar(argv, command = 'conectar', change_console_title = True)

    res = conector.run()

    if isinstance(res, str):
        print(res)
    elif isinstance(res, bool):
        if res:
            sys.exit(ExitStatus.success)
        else:
            sys.exit(ExitStatus.failure)
    elif isinstance(res, ExitStatus):
        sys.exit(res)
    else:
        sys.exit(ExitStatus.failure)


if __name__ == "__main__":
    main(sys.argv[1:])
