#!/bin/python2

import pwn

user = "bandit27"
host = "bandit.labs.overthewire.org"
passwd = "3ba3118a22e93127a4ed485be72ef5ea"
port = 2220

cmd = """  
# 1. mkdir /tmp/mybandit28
# 2. cd /tmp/mybandit28
# 3. git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
# 4. cd repo
# 5. cat /README | egrep -o "[a-zA-Z0-9]{32}"

echo "0ef186ac70e04ea33b4c1853d2526fa2"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit28", host, port, new_passwd)

print shell.ls()
