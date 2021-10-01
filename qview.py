#!/usr/bin/python3

import os
import sys
import data_qview

if ("-h" in sys.argv or len(sys.argv)<=1 or "--help" in sys.argv):
    print("""
  ___        _      _           _    __        __
 / _ \ _   _(_) ___| | ____   _(_) __\ \      / /
| | | | | | | |/ __| |/ /\ \ / / |/ _ \ \ /\ / /
| |_| | |_| | | (__|   <  \ V /| |  __/\ V  V /
 \__\_\__,__|_|\___|_|\_\  \_/ |_|\___| \_/\_/
     \_\\

""")
    print("\nqw {bind}")
    print("    --add")
    print("        Add bind")
    print("    --list")
    print("        Print list of binds")
    print("    --delete")
    print("        Delete bind")
    print("    -h")
    print("        This help")
    print("\n\nThanks!")
    sys.exit()

bind = data_qview.bind
command = data_qview.command

to_del = ""

if ("--list" in sys.argv):
    print("{0:10s} {1:10s}".format("Bind", "Command"))
    for i in range(len(command)):
        print("{0:10s} {1:10s}".format(bind[i], command[i]))
elif ("--delete" in sys.argv):
    to_del = " ".join(sys.argv).split("--delete ")[len(to_del)-1]
    print(to_del)
    for i in range(len(bind)):
        if to_del==bind[i]:
            print("\"{0}\" bind deleted.".format(bind[i]))
            bind.pop(i)
            command.pop(i)
            break
    os.system('echo "bind = %s" > /usr/bin/data_qview.py' % (str(bind)))
    os.system('echo "command = %s" >> /usr/bin/data_qview.py' % (str(command)))


elif ("--add" in sys.argv):
    bind.append(input("Bind: "))
    command.append(input("Command: "))
    os.system('echo "bind = %s" > /usr/bin/data_qview.py' % (str(bind)))
    os.system('echo "command = %s" >> /usr/bin/data_qview.py' % (str(command)))

u = " "

a_vars = []

if "-t" in sys.argv:
    for i in range(len(sys.argv)):
        if sys.argv[i]=="-t":
            a_vars = sys.argv[i+1:]

for i in range(len(command)):
    if "{}" in command[i]:
        cc = command[i].count("{}") + 1
    else:
        cc = 0
    if (bind[i]==u.join(sys.argv[1:len(sys.argv)-cc])):
        if "-t" in sys.argv:
            for k in range(len(a_vars)):
                command[i] = command[i].replace("{}", a_vars[k])
        if "{}" in command[i]:
            print("Not enought args given, command: {}".format(command[i]))
        else:
            print(command[i])
            os.system(command[i])
