#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    Desmontar

    @file       : desmontar.py
    @brief      : fuse.sshfs unmounting system for servers' home directory

    @author     : Veltys
    @date       : 2023-11-21
    @version    : 2.0.3
    @usage      : python desmontar.py -s server_or_group | python3 desmontar.py -s server_or_group | ./desmontar.py -s server_or_group
    @note       : ...
'''


from exitstatus import ExitStatus                                               # POSIX exit status codes
import sys                                                                      # System-specific parameters and functions

from libConectar import libConectar                                             # Connection library


def main(argv = sys.argv[1:]):
    '''!
        Performs the needed operations to unmount

        @param argv:    Program arguments

        @return:        Return code
    '''


    conector = libConectar(argv, command = 'desmontar')
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
