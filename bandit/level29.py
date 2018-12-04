#!/bin/python2

import pwn

user = "bandit28"
host = "bandit.labs.overthewire.org"
passwd = "0ef186ac70e04ea33b4c1853d2526fa2"
port = 2220

cmd = """  
# 1. mkdir /tmp/mybandit29
# 2. cd /tmp/mybandit29
# 3. git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
# 4. cd repo
# 5. cat /README.md
# 6. git log
# 7. git checkout commitID
# 8. cat /README.md
# 9. cd ~
# 10. rm -Rf /tmp/mybandit28

echo "bbc96594b4e001778eee9975372716b2"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit29", host, port, new_passwd)

print shell.ls()
