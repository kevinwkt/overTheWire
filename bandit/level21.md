# Level 21

For this challenge all we had to do was to use pipe the previous password using ```cat``` to a port we were listening to using ```nc```. After, we use the *./suconnect* file to obtain the password like the following:  

```
cat /etc/bandit_pass/bandit20 |  
nc -l -p 6000 &  
./suconnect 6000 |  
grep read  
```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit21@bandit.labs.overthewire.org```
