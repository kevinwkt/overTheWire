# Level 8

Since the the objective is to find the line with the word "millionth" in the only file in the server "./data.txt", we can use the following command to get the line:  

```grep millionth ./data.txt```  

The above will give the result:  

```millionth       passKey```  

To filter only the passKey, we can use the ```awk``` command to give us the second column using the following:  

```grep millionth ./data.txt | awk '{print $2}'```

Finally, we ssh to verify.  

```ssh -p 2220 bandit8@bandit.labs.overthewire.org```
