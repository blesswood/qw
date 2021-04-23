import os
import sys
import getpass

bind_list = []
command_list= []

print("""

  ___        _      _           _    __        __
 / _ \ _   _(_) ___| | ____   _(_) __\ \      / /
| | | | | | | |/ __| |/ /\ \ / / |/ _ \ \ /\ / /
| |_| | |_| | | (__|   <  \ V /| |  __/\ V  V /
 \__\_\__,__|_|\___|_|\_\  \_/ |_|\___| \_/\_/
     \_\\

\n
""")
print("\033[1;32;40mEnter bind-command key step by step\nAfter last binding add '##'\033[0;37;40m")

while True:
    bind = input("bind: ")
    if bind == "##":
        print("Ok")
        break
    else:
        command = input("command: ")
        bind_list.append(bind)
        command_list.append(command)

os.system("sudo rm /usr/bin/qw > /dev/null 2>&1")

os.system("touch data_qview.py")

os.system('echo "bind = %s" > data_qview.py' % (str(bind_list)))
os.system('echo "command = %s" >> data_qview.py' % (str(command_list)))


os.system("sudo cp data_qview.py /usr/bin && sudo chown %s /usr/bin/data_qview.py &&sudo chmod 755 /usr/bin/data_qview.py" % getpass.getuser())
os.system("sudo cp qview.py /usr/bin && sudo chmod 755 /usr/bin/qview.py && sudo chmod +x /usr/bin/qview.py")
os.chdir("/usr/bin")
os.system("sudo ln -s qview.py qw")
