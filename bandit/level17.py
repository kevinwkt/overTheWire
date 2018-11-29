#!/bin/python2

import pwn

user = "bandit16"
host = "bandit.labs.overthewire.org"
passwd = "cluFn7wTiGryunymYOu4RcffSxQluehd"
port = 2220

cmd = """
mkdir /tmp/mybandit17 &&
cat /etc/bandit_pass/bandit16 |
openssl s_client -connect localhost:"$(
nmap -sT -A -p 31000-32000 localhost | 
grep 'tcp open' | 
grep -v 'echo' |
xargs -n1 |
grep 'tcp' |
cut -c1-5)" -quiet 2>/dev/null > /tmp/mybandit17/bandit17.sshkey.private &&
chmod 400 /tmp/mybandit17/bandit17.sshkey.private &&
ssh -q -o StrictHostKeyChecking=no -i /tmp/mybandit17/bandit17.sshkey.private bandit17@localhost cat /etc/bandit_pass/bandit17 && 
rm -Rf /tmp/mybandit17
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvall().strip()

shell.close()

shell = pwn.ssh("bandit17", host, port, new_passwd)

print shell.ls()
