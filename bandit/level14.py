#!/bin/python2

import pwn

user = "bandit13"
host = "bandit.labs.overthewire.org"
passwd = "8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL"
port = 2220

cmd = "ssh -o StrictHostKeyChecking=no -i ./sshkey.private bandit14@localhost cat /etc/bandit_pass/bandit14 2>/dev/null"

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit14", host, port, new_passwd)

print shell.ls()
