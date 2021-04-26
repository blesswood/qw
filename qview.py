#!/usr/bin/python3

import os
import sys
import data_qview

if ("-h" in sys.argv or len(sys.argv)<=1 or "-h" in sys.argv):
    print("""
  ___        _      _           _    __        __
 / _ \ _   _(_) ___| | ____   _(_) __\ \      / /
| | | | | | | |/ __| |/ /\ \ / / |/ _ \ \ /\ / /
| |_| | |_| | | (__|   <  \ V /| |  __/\ V  V /
 \__\_\__,__|_|\___|_|\_\  \_/ |_|\___| \_/\_/
     \_\\

""")
    print("\nqw {bind}")
    print("qw --add-bind")
    print("\n\nThanks!")
    sys.exit()

bind = data_qview.bind
command = data_qview.command

if ("--add-bind" in sys.argv):
    bind.append(input("bind: "))
    command.append(input("command: "))
    os.system('echo "bind = %s" > /usr/bin/data_qview.py' % (str(bind)))
    os.system('echo "command = %s" >> /usr/bin/data_qview.py' % (str(command)))

u = " "
for i in range(len(command)):
    if ("%s" in command[i]):
        if sys.argv[len(sys.argv)-1]!=bind[i]:
            command[i] = command[i] % (str(sys.argv[len(sys.argv)-1]))
        else:
            command[i] = command[i] % u
    if (bind[i] in u.join(sys.argv)):
        os.system(command[i])
