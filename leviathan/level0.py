#!/bin/python2

import pwn

host = "leviathan.labs.overthewire.org"
user = "leviathan0"
passwd = "leviathan0"
port = 2223

cmd = """
cat /home/leviathan0/.backup/bookmarks.html | 
grep leviathan | 
egrep -o "[a-zA-Z0-9]{10}" |
head -2 |
tail -1
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()
print new_passwd

print shell.ls()
