# Level 4

We are given 2 files and are told that we must use a frequency analyzer to find the 6-letter key used to encrypt this.

We will start by counting all the letters and map from the most frequently used letters from the english language to the most frequently used letter from the 2 files we are given grouping the letters for every 6 letter found.

More details can be seen in the python script.


```
mkdir /tmp/username
cd /tmp/username
ln -s /krypton/krypton4/found1
ln -s /krypton/krypton4/found2
ln -s /krypton/krypton3/krypton5
# You can use vi/nano/etc
# You can find level3_count.py in this repo
vim level4_count.py
./count.py
# PERMUTE AND REPEAT UNTIL WE GET ANSWER
```

We then ssh to verify the passkey obtained above.

```ssh -p 2222 krypton5@krypton.labs.overthewire.org```
