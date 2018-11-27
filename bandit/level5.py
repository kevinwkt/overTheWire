#!/bin/python2

import pwn

user = "bandit4"
host = "bandit.labs.overthewire.org"
passwd = "pIwrPrtPN36QITSp3EQaw936yaFoFgAB"
port = 2220

cmd = """
for f in ./inhere/*; do
    if [ "$(file $f | grep -c ASCII)" -eq 1 ]; then
        cat "$f";
    fi
done;
"""

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit5", host, port, new_passwd)

print shell.ls()
