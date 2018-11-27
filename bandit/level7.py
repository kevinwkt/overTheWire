#!/bin/python2

import pwn

user = "bandit6"
host = "bandit.labs.overthewire.org"
passwd = "DXjZPULLxYr17uwoI01bNLQbtFemEgo7"
port = 2220

cmd = "find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null | xargs cat"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
print new_passwd
shell.close()

shell = pwn.ssh("bandit7", host, port, new_passwd)

print shell.ls()
