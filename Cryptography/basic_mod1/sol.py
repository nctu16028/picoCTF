#!/usr/bin/env python3

mapping = list("abcdefghijklmnopqrstuvwxyz0123456789_")

with open("message.txt", "r") as f:
    nums = f.read().split()
print(nums)

flag = ""
for num in nums:
    n = int(num) % 37
    flag += mapping[n]
print(flag)

