#!/bin/python2

import pwn

user = "bandit12"
host = "bandit.labs.overthewire.org"
passwd = "5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu"
port = 2220

cmd = """
mkdir /tmp/mybandit13 &&
cp data.txt /tmp/mybandit13 &&
cd /tmp/mybandit13 &&
xxd -r ./data.txt f &&
while [ "$(file ./f | grep -c ASCII)" -eq 0 ]; do
    if [ "$(file ./f | grep -c gzip)" -eq 1 ]; then
        mv f f.gz;
        gzip -q -d ./f.gz f;
    fi
    if [ "$(file ./f | grep -c bzip)" -eq 1 ]; then
        mv f f.bz2;
        bzip2 -q -d f.bz2 f 2>/dev/null;
    fi
    if [ "$(file ./f | grep -c tar)" -eq 1 ]; then
        mv f f.tz;
        tar -xf f.tz;
        rm f.tz;
        mv *.bin f;
    fi
done &&
cat ./f | xargs -n1 | awk 'length($0)>10' &&
cd ~ &&
rm -Rf /tmp/mybandit13
"""

shell = pwn.ssh(user, host, port, passwd)

new_passwd = shell.run(cmd).recvall().strip()
print new_passwd
shell.close()

shell = pwn.ssh("bandit13", host, port, new_passwd)

print shell.ls()
