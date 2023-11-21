#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    Conectar

    @file       : conectar.py
    @brief      : Server connection system

    @author     : Veltys
    @date       : 2023-11-21
    @version    : 2.0.3
    @usage      : python conectar.py -s server_or_group | python3 conectar.py -s server_or_group | ./conectar.py -s server_or_group
    @note       : ...
'''


from conector.libConectar import libConectar                                    # Connection library
from exitstatus import ExitStatus                                               # POSIX exit status codes
import sys                                                                      # System-specific parameters and functions


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

        return ExitStatus.success

    elif isinstance(res, bool):
        if res:
            return ExitStatus.success

        else:
            return ExitStatus.failure

    elif isinstance(res, ExitStatus):
        return res

    else:
        return ExitStatus.failure


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
