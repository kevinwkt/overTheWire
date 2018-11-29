#!/bin/python2

import pwn

user = "bandit18"
host = "bandit.labs.overthewire.org"
passwd = "kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd"
port = 2220

cmd = "ssh -q -o StrictHostKeyChecking=no bandit18@localhost 'cat ./readme'"

shell = pwn.ssh(user, host, port, passwd)
s = shell.run(cmd)
s.sendline(passwd)
s.sendline("cat ./readme")
s.recv()
new_passwd = s.recv().strip()

shell.close()

shell = pwn.ssh("bandit19", host, port, new_passwd)

print shell.ls()
