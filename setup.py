#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
NAME:
setupe.py

DESCRIPTION:
Install sysupdate.py to /usr/local/bin

CREATED:
25 Feb 2017

VERSION:
1

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
from shutil import copyfile

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

copyfile ('./sysupdate.py', '/usr/local/bin/sysupdate.py')

