# Level 22

Since the challenge told us to look at the /etc/cron.d/ directory, we ```ls``` it to see that there are 3 files:  

* cronjob_bandit22
* cronjob_bandit23
* cronjob_bandit24  

Because this is challenge 22, we open cronjob_bandit22 to see the following:   

```
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null  
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```  

We then ```cat``` into the */usr/bin/cronjob_bandit22.sh* to see the following:  

```
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv  
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```  

We see that the bandit_pass is sent to */tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv* so finally, we cat that file and ssh into the next level:  

```ssh -p 2220 bandit22@bandit.labs.overthewire.org```
