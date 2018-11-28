# Level 11

OvertheWire tells us the file is encoded with base64,so we use ```base64 -d``` to decode the contents. We then filter the contents to get rid of "words" less than around 10 characters in order to find the real passkey. One way to do this is to use ```tr``` or ```sed``` to make take the sentence and put them in separate lines in order to use ```awk 'length($0)>10'``` used previously to get the following:  

```base64 -d ./data.txt | xargs -n1 | awk 'length($0)>10'```  

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit11@bandit.labs.overthewire.org```
