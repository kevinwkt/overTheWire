#!/bin/python3
# This script only works with characters from A-Za-z. Any other letters will be ignored such as whitespaces and punctuation marks.

import sys

upper = 64
lower = 96
u_mask = 63

special_chars = set("!@#$%^&*()[]:;,<>./?~ 1234567890")

def rot(n):
    str = [ord(x) for x in input()]
    
    enc = ''
    for c in str:
        if chr(c) not in special_chars:
            enc += chr((c&lower)|((u_mask&c)+n)%26)
        else:
            enc += chr(c)

    print(enc)

def main():
    if len(sys.argv) != 2:
        print("Error in arguments")
        exit(0)
    rot(int(sys.argv[1]))

main()
