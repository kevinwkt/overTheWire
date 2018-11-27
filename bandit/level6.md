# Level 6

All we have to do is find the correct file with the given specification using the ```find``` command like the following:  

```find . -type f -size 1033c```

Once we find it, we can ```cat``` it or just pipe it like this:  
```find . -type f -size 1033c | xargs cat```

Finally, we ssh to verify.  

```ssh -p 2220 bandit6@bandit.labs.overthewire.org```
