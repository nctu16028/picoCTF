#!/usr/bin/env python3

with open("message.txt", "r") as f:
    ciphertext = f.read()
key = ciphertext.split()[0]

trans = dict()
for i, c in enumerate(key):
    trans[c] = chr(ord("A") + i)
    trans[c.lower()] = chr(ord("a") + i)
print(trans)

flag = ''.join([
    trans[c]
    if c in trans else c
    for c in ciphertext
])
print(flag)

