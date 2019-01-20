#!/bin/python3
# Accepted alphabet is [a-zA-Z] and [:space:]

import sys

# Hardcode for ASCII

b1 = 96 # 96 is int for b'1100000'
b2 = 31 # 31 is int for b'0011111'

# Hardcode for special characters

sp = set("!@#$%^&*()[]:;,<>./?~ 1234567890")

def decrypt(m, k):
    crypt = [ord(x) for x in m]

    key = [ord(x) for x in k]

    ans = ""
    j = 0
    for i in range(len(crypt)):
        if chr(crypt[i]) in sp:
            ans += chr(crypt[i])
        else:
            ans += chr(crypt[i]&96|((crypt[i]&b2)-(key[j%len(key)]&b2)+27)%26)
            j += 1
    return ans

def encrypt(m, k):
    messg = [ord(x) for x in m]

    key = [ord(x) for x in k]

    ans = ""
    j = 0
    for i in range(len(messg)):
        if chr(messg[i]) in sp:
            ans += chr(messg[i])
        else:
            ans += chr(messg[i]&96|((messg[i]&b2)+(key[j%len(key)]&b2)-1)%26)
            j += 1
    return ans

def main():
    if sys.argv[1] == '-e':
        encrypt()
    elif sys.argv[1] == '-d':
        decrypt()

