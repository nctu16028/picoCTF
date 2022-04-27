#!/usr/bin/env python3

with open("leak/usernames.txt", "r") as f:
    users = f.read().split()

with open("leak/passwords.txt", "r") as f:
    creds = f.read().split()

comb = dict(zip(users, creds))
print(comb["cultiris"])
flag = ""
for c in comb["cultiris"]:
    if c >= 'A' and c <= 'Z':
        c_ = chr(ord('A') + ((ord(c)-ord('A')) + 13) % 26)
        flag += c_
    elif c >= 'a' and c <= 'z':
        c_ = chr(ord('a') + ((ord(c)-ord('a')) + 13) % 26)
        flag += c_
    else:
        flag += c
print(flag)

