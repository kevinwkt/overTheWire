# Level 5

We can just iterate through each file in the directory *./inhere* and just use  
```file ./-fileNo``` and check if we get the following:  

```./-fileNo: ASCII text```

Once we find that file, just ```cat ./-fileNo``` and use it in the following:

```ssh -p 2220 bandit5@bandit.labs.overthewire.org```
