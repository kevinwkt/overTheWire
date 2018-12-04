#!/bin/python2

import pwn
import re

user = "bandit25"
host = "bandit.labs.overthewire.org"
passwd = "uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG"
port = 2220

cmd = """  
# 1. We make the terminal small enough
# 2. We press 'v'
# 3. We write ':set shell sh=/bin/bash'
# 4. We write 'sh'
# 5. ls
# 6. ./bandit27-do cat /etc/bandit_pass/bandit27
echo "3ba3118a22e93127a4ed485be72ef5ea"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit27", host, port, new_passwd)

print shell.ls()
