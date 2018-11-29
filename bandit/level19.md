# Level 19

Given that when using ```ssh``` we get logged out, we send ```cat``` on the file with the ```ssh``` like the following:  

```ssh -q -o StrictHostKeyChecking=no bandit18@localhost 'cat ./readme'```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit19@bandit.labs.overthewire.org```
