#!/usr/bin/env python3

import string

UPPERCASE_OFFSET = ord("A")
ALPHABET = string.ascii_uppercase

def shift(c, k):
    t1 = ord(c) - UPPERCASE_OFFSET
    t2 = ord(k) - UPPERCASE_OFFSET
    return ALPHABET[(len(ALPHABET) + t1 - t2) % len(ALPHABET)]

cipher = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

plain = ""
for i, c in enumerate(cipher):
    plain += shift(c, key[i])
print(plain)

