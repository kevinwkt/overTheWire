# Level 26

We first try to get into bandit26@localhost using the ssh file we found with the following command:  

```ssh -i ./bandit26.sshkey -o StrictHostKeyChecking=no bandit26@localhost```  

When we use the command above, we see the following:  

```<pre>
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
Connection to localhost closed.
```</pre>

We realize that we are logged out immediately. So we check the "/etc/passwd" to check for the login shell for bandit26 with the following:  

```cat /etc/passwd | grep bandit26 ```  

We then see the following script being run:  

```bandit26:x:11026:11026:bandit level 26:/home/bandit26:*/usr/bin/showtext*```  

We now cat "/usr/bin/showtext" to see the following code:  

```
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

We can then assume that when you log in, ```sh``` is run and then ```more```, where the text above will
probably be seen. We now have to find a way to see the password before it logs us out with the ```exit 0``` 
code. To do this, we use ```more``` to go to VISUALMODE by changing the terminal size super small so that 
more doesn't get to show us everything so it will wait for us to call on ```vi``` presing on the "v" button.

So basically enter vi by:  
1. We make the terminal small enough for it to not be able to print "bandit26".
2. We ssh into bandit26 as normal.
3. We press "v" while more is waiting for user to enter vi.

Once in vi, we set "/bin/bash" as sh and we invoke it:  
1. ```:set shell sh=/bin/bash```
2. ```sh```  

Once we are running bash, we get the passkey by running the usual:  

```cat /etc/bandit_pass/bandit26```

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit26@bandit.labs.overthewire.org```
