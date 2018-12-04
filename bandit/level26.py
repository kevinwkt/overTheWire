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
# 5. cat /etc/bandit_pass/bandit26
echo "5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvline_regex(re.compile("[a-zA-Z0-9]{32}")).strip()

shell.close()

shell = pwn.ssh("bandit26", host, port, new_passwd)

print shell.ls()
