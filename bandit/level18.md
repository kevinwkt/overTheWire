# Level 18

For this challenge all we had to do was use ```diff``` and use the passkey found in *passwords.new* like the following:  

```diff ./passwords.old ./passwords.new | grep ">" | cut -c3-36```

Finally, we ssh to verify the passkey obtained above.  

```ssh -p 2220 bandit18@bandit.labs.overthewire.org```
