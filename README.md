# qw
QuickViewer  
Simplify large commands, using qw 

Installing:  
python3 setup_qview.py  
Then set bindings you want step by step (bind-command), after last edition add "##" (without quotes)  

Using:  
qw {bind}  
  
Help:  
qw  
    --add  
        Add bind  
    --list  
        Print list of binds  
    --delete  
        Delete bind  
  
Example:  
qw --add  
Bind: dkr  
Command: ssh root@192.168.1.43 docker ps  
  
[root@192.168.1.42 ~]$ qw dkr  
CONTAINER ID        IMAGE                                                                    COMMAND                  CREATED             STATUS              PORTS               NAMES  
  
  
Bugs:  
set fileformat to "unix" if you see "bash: /usr/bin/qw: /usr/bin/python3^M: bad interpreter: No such file or directory"
