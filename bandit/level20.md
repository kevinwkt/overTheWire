# Level 20

After running *./bandit20-do*, we see the following:  

```
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
```  

Then we just use that binary to run ```cat``` on the password file like the following:  

```./bandit20-do cat /etc/bandit_pass/bandit20```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit20@bandit.labs.overthewire.org```
