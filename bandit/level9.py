#!/bin/python2

import pwn

user = "bandit8"
host = "bandit.labs.overthewire.org"
passwd = "cvX2JJa4CFALtqS87jk27qwqGhBM9plV"
port = 2220

cmd = "sort ./data.txt | uniq -u"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit9", host, port, new_passwd)

print shell.ls()
