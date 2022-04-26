#!/usr/bin/env python3

from Crypto.Util.number import inverse
mapping = list(" abcdefghijklmnopqrstuvwxyz0123456789_")

with open("message.txt", "r") as f:
    nums = f.read().split()
print(nums)

flag = ""
for num in nums:
    n = inverse(int(num), 41)
    flag += mapping[n]
print(flag)

