#!/usr/bin/env python3

import hashlib

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

correct_pw_hash = open('level5.hash.bin', 'rb').read()
pos_pw_list = open('dictionary.txt', 'r').readlines()

for pw in pos_pw_list:
    hash_val = hash_pw(pw.strip())  # strip() to remove '\n'
    if hash_val == correct_pw_hash:
        print(f"Correct password: {pw}")
        break

