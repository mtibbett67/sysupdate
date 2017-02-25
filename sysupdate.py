#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
NAME:
sysupdate.py

DESCRIPTION:
Update OS using apt

CREATED:
Tue Mar 17 22:17:50 2015

VERSION:
2

AUTHOR:
Mark Tibbett

AUTHOR_EMAIL:
mtibbett67@gmail.com

URL:
N/A

DOWNLOAD_URL:
N/A

INSTALL_REQUIRES:
[]

PACKAGES:
[]

SCRIPTS:
[]

'''

# Standard library imports
import os
import sys
import subprocess

# Related third party imports


# Local application/library specific imports


# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

# Section formats
SEPARATOR = B + '=' * 80 + W
NL = '\n'

# Clear the terminal
os.system('clear')

# Check for root or sudo.  Remove if not needed.
UID = os.getuid()

if UID != 0:
    print R + ' [!]' + O + ' ERROR:' + G + ' sysupdate' + O + \
    ' must be run as ' + R + 'root' + W
#    print R + ' [!]' + O + ' login as root (' + W + 'su root' + O + ') \
#    or try ' + W + 'sudo ./wifite.py' + W

    os.execvp('sudo', ['sudo'] + sys.argv)

else:
    print NL
    print G + 'You are running this script as ' + R + 'root' + W
    print NL + SEPARATOR + NL

    def apt(arg1, arg2):
        '''Run apt to update system'''
        print arg1 + NL
        subprocess.call(['apt-get', arg2])

    apt(G + 'Retrieving new lists of packages' + W, 'update')
    print NL + SEPARATOR + NL
    apt(G + 'Performing dist-upgrade' + W, 'dist-upgrade')
    print NL + SEPARATOR + NL
    apt(G + 'Performing upgrades' + W, 'upgrade')
    print NL + SEPARATOR + NL
    apt(G + 'Erasing downloaded archive files' + W, 'clean')
    print NL + SEPARATOR + NL
    apt(G + 'Erasing old downladed archive files' + W, 'autoclean')
    print NL + SEPARATOR + NL
    apt(G + 'Removing all unused packages' + W, 'autoremove')
    print NL + SEPARATOR + NL
