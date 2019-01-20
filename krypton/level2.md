# Level 2

The instructions for this challenge tells us that the password is in ROT13. We can use the script I wrote rot to solve this problem again using a bash script:

```
cat krypton3 |
for i in `seq 1 25`;
do
# substitute "cat krypton3" with the actual encoded message; echo 'result_of_cat_krypton3'
    cat krypton3 | ./rot.py $i
done
```

With this script we get many results, but we can tell pretty easily which one is the passkey.


As an alternative, we can also use the suggested method by doing the following:

```
mktmp -d
cd 'new_dir_created'
ln -s /krypton/krypton2/keyfile.dat
chmod 777 .
echo "ABYZ" > tmp.txt
/krypton/krypton2/encrypt tmp.txt
cat ciphertext
```

With the method above, we encrypt "ABYZ" and we check the cipher text to see the shift value.


We then ssh to verify the passkey obtained above.

```ssh -p 2222 krypton3@krypton.labs.overthewire.org```


