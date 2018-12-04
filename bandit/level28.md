# Level 28

We create a directory since we must use ```git clone``` along with the previous password to download a folder with the passkey:  

```
mkdir /tmp/mybandit28
cd /tmp/mybandit28
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```  

Once we get the folder, we ```cd``` into it ```cat``` the "README" file and filter the result like the following:  

```
cd repo
cat README | egrep -o "[a-zA-Z0-9]{32}"
rm -Rf /tmp/mybandit28
```

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit28@bandit.labs.overthewire.org```
