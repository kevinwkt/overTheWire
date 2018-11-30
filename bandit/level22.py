#!/bin/python2

import pwn

user = "bandit21"
host = "bandit.labs.overthewire.org"
passwd = "gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr"
port = 2220

cmd = """  
cat "$(
    cat "$(
        cat /etc/cron.d/cronjob_bandit22 | 
        tr ' ' '\n' | 
        grep .sh | 
        head -1
    )" | 
    tr ' ' '\n' | 
    awk 'length($1)>31' | 
    head -1
)"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit22", host, port, new_passwd)

print shell.ls()
