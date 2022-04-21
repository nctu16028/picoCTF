#!/usr/bin/env python3

with open("flag.en", "r") as f:
    flag_en = f.readline().strip()

print(flag_en)

flag = ""
for c in flag_en:
    if c >= 'A' and c <= 'Z':
        c_ = chr(ord('A') + ((ord(c)-ord('A')) + 13) % 26)
        flag += c_
    elif c >= 'a' and c <= 'z':
        c_ = chr(ord('a') + ((ord(c)-ord('a')) + 13) % 26)
        flag += c_
    else:
        flag += c
print(flag)

