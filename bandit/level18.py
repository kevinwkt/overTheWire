#!/bin/python2

import pwn
import nmap

user = "bandit17"
host = "bandit.labs.overthewire.org"
passwd = "xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn"
port = 2220

cmd = "diff ./passwords.old ./passwords.new | grep '>' | cut -c3-36" 

shell = pwn.ssh(user, host, port, passwd)
new_passwd = shell.run(cmd).recvall().strip()

shell.close()

shell = pwn.ssh("bandit18", host, port, new_passwd)

print shell.ls()
