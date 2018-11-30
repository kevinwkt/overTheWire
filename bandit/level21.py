#!/bin/python2

import pwn

user = "bandit20"
host = "bandit.labs.overthewire.org"
passwd = "GbKksEFF4yrVs6il55v6gwY5aVje5f0j"
port = 2220

cmd = """  
cat /etc/bandit_pass/bandit20 |
nc -l -p 6000 &
./suconnect 6000 |
grep read
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit21", host, port, new_passwd)

print shell.ls()
