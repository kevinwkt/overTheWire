#!/bin/python2

import pwn

user = "bandit11"
host = "bandit.labs.overthewire.org"
passwd = "IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR"
port = 2220

cmd = "cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | xargs -n1 | awk 'length($0)>10'"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit12", host, port, new_passwd)

print shell.ls()
