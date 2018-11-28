# Level 14

All we have to do in this challenge is log into localhost as bandit14 using the ssh.private key. To do this we use the following command *(2>/dev/null, 2 means stderr and /dev/null is just trash)*:  

```ssh -o StrictHostKeyChecking=no -i ./sshkey.private bandit14@localhost cat /etc/bandit_pass/bandit14 2>/dev/null```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit14@bandit.labs.overthewire.org```
