#!/usr/bin/env python3

with open("message.txt", "r") as f:
    ciphertext = f.read()
print(ciphertext)

flag = ""
for i in range(len(ciphertext) // 3):
    flag += ciphertext[3 * i + 2]
    flag += ciphertext[3 * i]
    flag += ciphertext[3 * i + 1]
print(flag)

