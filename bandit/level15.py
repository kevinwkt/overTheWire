#!/bin/python2

import pwn

user = "bandit14"
host = "bandit.labs.overthewire.org"
passwd = "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e"
port = 2220

cmd = "echo '"+passwd+"' | nc localhost 30000 | awk 'length($0)==32'"

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvall().strip()
shell.close()

shell = pwn.ssh("bandit15", host, port, new_passwd)

print shell.ls()
