#!/bin/python2
import pwn

host = "bandit.labs.overthewire.org"
user = "bandit0"
passwd = "bandit0"
port = 2220

shell = pwn.ssh(user, host, port, passwd)

print shell.ls()


