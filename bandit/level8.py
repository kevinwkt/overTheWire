#!/bin/python2

import pwn

user = "bandit7"
host = "bandit.labs.overthewire.org"
passwd = "HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs"
port = 2220

cmd = "grep millionth ./data.txt | awk '{print $2}'"

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit8", host, port, new_passwd)

print shell.ls()
