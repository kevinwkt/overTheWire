#!/bin/python2

import pwn

user = "bandit10"
host = "bandit.labs.overthewire.org"
passwd = "truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk"
port = 2220

cmd = "base64 -d ./data.txt | xargs -n1 | awk 'length($0)>10'"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit11", host, port, new_passwd)

print shell.ls()
