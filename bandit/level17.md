# Level 17

For this challenge, first we use ```nmap``` to scan for open ports from 31000 to 32000 which uses *ssl* with the following command:  

```nmap -sT -A -p 31000-32000 localhost```  

We then use the port which does not have the action *echo* and use it as the port where we send our previous password using ```openssl``` like the following:  

openssl s_client -connect localhost:PORTNO -quiet 2>/dev/null  

Because the above gives us a RSA key, we save it in a file and use it as the key to ```ssh``` into bandit17 and just ```cat``` the corresponding key:  
```
openssl s_client -connect localhost:PORTNO -quiet 2>/dev/null -quiet 2>/dev/null > /tmp/mybandit17/bandit17.sshkey.private &&   
chmod 400 /tmp/mybandit17/bandit17.sshkey.private &&  
ssh -q -o StrictHostKeyChecking=no -i /tmp/mybandit17/bandit17.sshkey.private bandit17@localhost cat /etc/bandit_pass/bandit17 
```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit17@bandit.labs.overthewire.org```
