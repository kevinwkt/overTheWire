#!/bin/python2

import pwn

user = "bandit5"
host = "bandit.labs.overthewire.org"
passwd = "koReBOKuIDDepwhWk7jZC0RTdopnAYKh"
port = 2220

cmd = "find . -type f -size 1033c | xargs cat"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
print new_passwd
shell.close()

shell = pwn.ssh("bandit6", host, port, new_passwd)

print shell.ls()
