# Level 4

First we do ```ls -a``` and notice that there's a hidden folder called "inhere" as indicated in the description.  
We then enter the directory by using ```cd ./inhere``` and use ```ls -a``` once again to find a *.hidden* file.  

Finally, we enter bandit4 the same way as before by simply using ```cat``` with the file found above:  

```cat ./hidden```

and finally,  

```ssh -p 2220 bandit4@bandit.labs.overthewire.org```
