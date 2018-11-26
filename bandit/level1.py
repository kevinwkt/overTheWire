#!/bin/python2

import pwn

host = "bandit.labs.overthewire.org"
user = "bandit0"
passwd = "bandit0"
port = 2220

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run('cat "$(ls)"').recvall().strip("\n")
shell.close()

shell = pwn.ssh("bandit1", host, port, new_passwd)

print shell.ls()
