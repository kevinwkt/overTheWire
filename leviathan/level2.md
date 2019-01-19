# Level 1

We go to home directory and enter the "leviathan1" directory and use ```ls``` to
find a binary called "check". We then try running it but we see the following
after we enter any incorrect password:  

```
password:
Wrong password, Good Bye ...
```  

We then use ```strings``` and found some strings which were tried ```ssh```ing
into level2 without success. We then use ```ltrace``` to see the following:  

```
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x804853b, 1, 0xffffd774, 0x8048610 <unfinished ...>
printf("password: ")                                     = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: **mypasswordinput**
)                    = 112
getchar(1, 0, 0x65766f6c, 0x646f6700)                    = 97
getchar(1, 0, 0x65766f6c, 0x646f6700)                    = 115
strcmp("**myp**", "**password_for_check**")                                 = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                     = 29
+++ exited (status 0) +++
```  

We now run ```check``` by using what we found above as password which opens a
shell where we can finally ```cat``` the "/etc/leviathan_pass/leviathan2" and
get the passkey.

We then use ```ssh``` into the next level:  

```ssh -p 2223 leviathan2@leviathan.labs.overthewire.org```
