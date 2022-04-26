#!/usr/bin/env python3

from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

with open("ciphertext", "r") as f:
    z = f.read().split()

n = int(z[1])
e = int(z[3])
c = int(z[6])
print("n =", n)
print("e =", e)
print("c =", c)

for k in range(1000000):
    m, has_root = iroot(c + k * n, e)   # Find (c+k*n) ^ (1/e) if exist
    if has_root:
        print("m =", m)
        break

flag = long_to_bytes(m).decode()
print(flag)

