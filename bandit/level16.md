# Level 16

We only have to pipe the passkey to the ```openssl``` command and filter the results like the following:

```echo 'passkey' | openssl s_client -connect localhost:30001 -quiet``` 

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit16@bandit.labs.overthewire.org```
