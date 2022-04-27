#!/usr/bin/env python3

with open("cipher.txt", "r") as f:
    ciphertext = f.read().strip()
print(ciphertext)

key = "CYLAB"

flag = ""
key_idx = 0
for c in ciphertext:
    if c.isupper():
        C = ord(c) - ord("A")
        K = ord(key[key_idx]) - ord("A")
        M = (C + 26 - K) % 26
        m = chr(M + ord("A"))
        flag += m
        key_idx = (key_idx + 1) % len(key)
    elif c.islower():
        C = ord(c) - ord("a")
        K = ord(key[key_idx]) - ord("A")
        M = (C + 26 - K) % 26
        m = chr(M + ord("a"))
        flag += m
        key_idx = (key_idx + 1) % len(key)
    else:
        flag += c
print(flag)

