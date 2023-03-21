#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''!
    setup

    @file       : setup.py
    @brief      : Package installer

    @author     : Veltys
    @date       : 2023-03-17
    @version    : 1.0.0
    @usage      : (run by pip when the package is installed)
    @note       : ...
'''


from setuptools import setup, find_packages                                     # Easily download, build, install, upgrade, and uninstall Python packages

from install_script import CustomInstall

VERSION = '3.0.0'
DESCRIPTION = 'Python-powered system connection manager and mounts via SSH'
LONG_DESCRIPTION = 'System connection manager using Python which connects and mounts home directory through SSH'

setup(
    name = 'conector',
    version = VERSION,
    author = 'Veltys',
    author_email = '<veltys@veltys.es>',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    package_data = {
        'conector': ['bash_completion/*'],
    },
    install_requires = ['exitstatus'],
    cmdclass = {
        "install": CustomInstall,
    },
    keywords = ['python', 'connector', 'ssh'],
    entry_points = {
        'console_scripts': [
        'conectar = conector.conectar:main',
        'desmontar = conector.desmontar:main',
        'montar = conector.montar:main',
        ],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Spanish',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        # 'Operating System :: MacOS',                                          # TODO: Do some test before activating this
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System',
        'Topic :: System :: Networking',
        'Topic :: System :: Shells',
    ],
)
