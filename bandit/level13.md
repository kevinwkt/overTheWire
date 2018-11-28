# Level 13

Given a text hex dump, we reverse it back to binary by using the ```xxd``` command with the reverse *-r* flag. Then we keep on checking the file type by using the ```file``` command and use the following commands ```tar, bzip2, gzip``` repectively depending on what we need to decompress until we end up with a text file with the password. Once we reach the text file, we use the previous commands ```xargs``` and ```awk``` to get the passkey.

The following is the script used in my python script where I ```cat``` the passkey in the end:  

```
xxd -r ./data.txt f &&  
while [ "$(file ./f | grep -c ASCII)" -eq 0 ]; do  
    if [ "$(file ./f | grep -c gzip)" -eq 1 ]; then  
        mv f f.gz;  
        gzip -q -d ./f.gz f;  
    fi  
    if [ "$(file ./f | grep -c bzip)" -eq 1 ]; then  
        mv f f.bz2;  
        bzip2 -q -d f.bz2 f 2>/dev/null;  
    fi  
    if [ "$(file ./f | grep -c tar)" -eq 1 ]; then  
        mv f f.tz;  
        tar -xf f.tz;  
        rm f.tz;  
        mv *.bin f;  
    fi  
done &&  
cat ./f | xargs -n1 | awk 'length($0)>10'  ] ] ] ]  
```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit13@bandit.labs.overthewire.org```
