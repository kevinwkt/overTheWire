# Level 27

All we do here is use ```ls``` to see which files are currently present to see a file called "bandit27-do".

We use ```file``` and we see the following:  

```
bandit27-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8e941f24b8c5cd0af67b22b724c57e1ab92a92a1, not stripped
```

Since it's a binary, we run it and we see that it's the same binary used in previous challenges. We run the following command to get the passkey:  

```./bandit27-do cat /etc/bandit_pass/bandit27```

Finally, we ssh to verify the passkey obtained above.

```ssh -p 2220 bandit27@bandit.labs.overthewire.org```
