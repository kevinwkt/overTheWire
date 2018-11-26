#!/bin/python2

import pwn

host = "bandit.labs.overthewire.org"
user = "bandit1"
passwd = "boJ9jbbUNNfktd78OOpsqOltutMc3MY1"
port = 2220

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run('cat ./"$(ls)"').recvall().strip("\n")
shell.close()

shell = pwn.ssh("bandit2", host, port, new_passwd)

print shell.ls()
