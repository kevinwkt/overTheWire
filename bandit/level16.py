#!/bin/python2

import pwn

user = "bandit15"
host = "bandit.labs.overthewire.org"
passwd = "BfMYroe26WYalil77FoDi9qh59eK5xNr"
port = 2220

cmd = "echo '"+passwd+"' | openssl s_client -connect localhost:30001 -quiet" 

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvall().split('\n')[-3].strip()
shell.close()

shell = pwn.ssh("bandit16", host, port, new_passwd)

print shell.ls()
