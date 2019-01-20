# Level 3

We are given 3 files and are told that we must use a frequency analyzer to find the key used to encrypt this.

We will start by counting all the letters and map from the most frequently used letters from the english language to the most frequently used letter from the 3 files we are given.

```
mkdir /tmp/username
cd /tmp/username
ln -s /krypton/krypton3/found1
ln -s /krypton/krypton3/found2
ln -s /krypton/krypton3/found3
# You can use vi/nano/etc
# You can find level3_count.py in this repo
vim level3_count.py
./count.py
# REPEAT UNTIL WE GET ANSWER
```

We then ssh to verify the passkey obtained above.

```ssh -p 2222 krypton4@krypton.labs.overthewire.org```
