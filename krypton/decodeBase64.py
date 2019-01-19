#!/bin/python3

import sys

base = 96 
lower = 96
upper = 64
number = 48

def table(n):
    if n == 62: return '+'
    if n == 63: return '/'
    if n < 26: return chr(upper+n+1)
    if n < 52: return chr(lower+(n-25))
    return chr(number+n-52)

def rtable(c):
    if c == '/': return 63
    if c == '+': return 62
    if c <= '9': return (ord(c)^number)+52
    if c <= 'Z': return (ord(c)^upper)-1
    return (ord(c)^lower)+25

def encrypt():
    str = input()

    bStr = ''
    for c in str:
        if c != ' ' or c != '\n' or c != ',': 
            bStr += format(ord(c),'08b')

    encoded = ''
    for i in range(0,len(bStr)//6):
        encoded += table(int(bStr[i*6:i*6+6],2))
    
    if len(bStr)%6 == 2:
        encoded += table(int(bStr[(len(bStr)//6)*6:]+"0000",2))
        encoded += "=="
    if len(bStr)%6 == 4:
        encoded += table(int(bStr[(len(bStr)//6)*6:]+"00",2))
        encoded += "="
    print(encoded)

def decrypt():
    str = input()

    bStr = ''
    for c in str:
        if c != '=':
            bStr += format(rtable(c),'06b')
    
    decoded = ''
    for i in range(0,len(bStr)//8):
        decoded += chr(int(bStr[i*8:(i*8)+8] ,2))

    print(decoded)


def main():
    if sys.argv[1] == '-d': decrypt()
    elif sys.argv[1] == '-e': encrypt()
    else: print("Error with flags")

main()
