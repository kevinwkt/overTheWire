# Level 29

We create a directory since we must use ```git clone``` along with the previous password to download a folder with the passkey:  

```
mkdir /tmp/mybandit29
cd /tmp/mybandit29
git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
```  

Once we get the folder, we ```cd``` into it ```cat``` the "README.md" file and filter the result like the following:  

```
cd repo
cat README.md
```

We then realize that the password has been changed to the following:  

``` <pre>
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
</pre> ```

So we use ```git log``` to see past commits. We then see 3 results:  

```
commit 073c27c130e6ee407e12faad1dd3848a110c4f95
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    fix info leak

commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

commit b67405defc6ef44210c53345fc953e6a21338cc7
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    initial commit of README.md
```

Because we believe that the password is in "add missing data" commit, we use ```git checkout``` and finally ```cat``` on the "README.md" file:  

```
git checkout 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
cat ./README.md
cd ~
rm -Rf /tmp/mybandit28
```

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit29@bandit.labs.overthewire.org```
