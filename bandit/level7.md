# Level 7

All we have to do is find the correct file with the given specification using the ```find``` command like the following:  

```find / -type f -size 33c -user bandit7 -group bandit6```

However, we get a lot of errors along with the correct file which says:
*find: '.../fileName': Permission denied*  

We can filter these out by using the following command:
```find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null```

Once we find it, we can ```cat``` it or just pipe it like this:  
```find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null | xargs cat```

Finally, we ssh to verify.  

```ssh -p 2220 bandit7@bandit.labs.overthewire.org```
