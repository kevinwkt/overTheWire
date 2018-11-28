# Level 10

First, we abstract all the readable strings by using ```strings``` command on the file. We then filter out the lines which have "==" on them since the website says *beginning with several ‘=’ characters* which implies more than 1 '='. Finally, we use ```awk``` to filter the answer with sufficient length like the following:  

```strings -d data.txt | egrep == | awk '{print $2}' | awk 'length($0)>10'```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit10@bandit.labs.overthewire.org```
