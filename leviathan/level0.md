# Level 0

First we ```ssh``` into "leviathan0@leviathan.labs.overthewire.org" using the following:  

```ssh -p 2223 leviathan0@leviathan.labs.overthewire.org```  

We then go to home directory and enter the "leviathan0" directory and use ```ls```:  

```
cd /home/leviathan0
ls
```  

After seeing that the folder was empy, we check for hidden folders using the "-a" flag and go into the ".backup" folder:  

```
ls -a
cd .backup/
```

We then find the "bookmarks.html" file where we use ```cat``` and ```grep``` for references of "leviathan":  

```cat bookmarks.html | grep leviathan```  

We then find the following passkey embedded:  

```
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed 
later, the password for leviathan1 is **PASSWORD**" ADD_DATE="1155384634" LAST_CHARSET=
"ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

We then use ```ssh``` into the next level:  

```ssh -p 2223 leviathan1@leviathan.labs.overthewire.org```
