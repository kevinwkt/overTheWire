# Level 1

The instructions for this challenge tells us that the passowrd is in ROT13. We can use the script I wrote rot to solve this problem:

```cat krypton2 | ./rot 13```


As an alternative, we can also use the ```tr``` command for this like the following:

```cat krypton2 | tr 'A-Za-z' 'N-ZA-Mn-za-m'```


We then ssh to verify the passkey obtained above.

```ssh -p 2222 krypton2@krypton.labs.overthewire.org```


