#!/bin/python2

import pwn

host = "bandit.labs.overthewire.org"
user = "bandit3"
passwd = "UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK"
port = 2220

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run('cd ./inhere && cat "$(ls -a | egrep .[a-z]+)"').recvall().strip("\n")
shell.close()

print new_passwd
shell = pwn.ssh("bandit4", host, port, new_passwd)

print shell.ls()
