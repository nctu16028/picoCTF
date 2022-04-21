#!/usr/bin/env python3

key = 25
with open("ciphertext", "r") as f:
    flag_en = f.read()

ct = flag_en[8:-1]  # remove "picoCTF{}"
print(ct)

flag = ""
for c in ct:
    if c >= 'A' and c <= 'Z':
        c_ = chr(ord('A') + ((ord(c)-ord('A')) + key) % 26)
        flag += c_
    elif c >= 'a' and c <= 'z':
        c_ = chr(ord('a') + ((ord(c)-ord('a')) + key) % 26)
        flag += c_
    else:
        flag += c
print("picoCTF{%s}" % flag)

