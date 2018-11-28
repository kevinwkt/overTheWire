# Level 15

All we have to do is pipe the previous answer to the ```nc``` command as like the following, and then we use the previous methods to filter the answer:

```echo 'passwd' | nc localhost 30000 | awk 'length($0)==32'```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit15@bandit.labs.overthewire.org```
