# Level 23

We first ```cat``` */etc/cron.d/cronjob_bandit23* to see the following:  

```
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```  

We then ```cat``` into the */usr/bin/cronjob_bandit23.sh* to see the following:  

```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```  

We see that the bandit_pass is sent to ```/tmp/"$(echo I am user "$(myname)" | md5sum | cut -d ' ' -f 1)"``` but we realize that ```"$(myname)"``` has to be bandit23 for this to work. So all we have to do is substitutde ```$(myname)``` with "bandit23". *Implementation of this can be seen in the python script*  

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit23@bandit.labs.overthewire.org```
