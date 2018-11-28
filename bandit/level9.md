# Level 9

Since the website notifies us that the passkey is the only one that does not repeat itself in the "data.txt" file, we can sort the file and use the ```uniq -u``` command like the following:  

```sort ./data.txt | uniq -u```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit9@bandit.labs.overthewire.org```
