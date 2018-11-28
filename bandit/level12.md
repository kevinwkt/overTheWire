# Level 12

We use ```tr``` to give offsets for each letter and do the same as previous challenges like the following:  

```cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | xargs -n1 | awk 'length($0)>10'```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit12@bandit.labs.overthewire.org```
