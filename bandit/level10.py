#!/bin/python2

import pwn

user = "bandit9"
host = "bandit.labs.overthewire.org"
passwd = "UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR"
port = 2220

cmd = "strings -d data.txt | egrep == | awk '{print $2}' | awk 'length($0)>10'"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit10", host, port, new_passwd)

print shell.ls()
