# Level 0

Given the encoded string 'S1JZUFRPTklTR1JFQVQ=' using Base64, we decode it using the script I wrote for encoding and decoding base64 (wrote it for fun and to practice).

```echo "S1JZUFRPTklTR1JFQVQ=" | ./decodeBase64.py -d```

and we get the flag!!!

If you want to do this the more boring way, we can just 
```echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d```
on most linux machines.


We then ssh to verify the passkey obtained above.

```ssh -p 2222 krypton1@krypton.labs.overthewire.org```


