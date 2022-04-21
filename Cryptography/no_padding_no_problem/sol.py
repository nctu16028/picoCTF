#!/usr/bin/env python3

from Crypto.Util.number import inverse, long_to_bytes
from pwn import *

ip = "mercury.picoctf.net"
port = 10333

context.log_level = "error"
r = remote(ip, port)

z = r.recvuntil(b"n: ").decode()
#print(z)
n = int(r.recvuntil(b"\ne: ", drop=True).decode())
print("n =", n)
e = int(r.recvuntil(b"\nciphertext: ", drop=True).decode())
print("e =", e)
c = int(r.recvuntil(b"\n\n\nGive me ciphertext to decrypt: ", drop=True).decode())
print("c =", c)

c_prime = (c * pow(2, e, n)) % n    # c' = cx^e mod n
print("c' =", c_prime)
r.sendline(str(c_prime).encode())
z = r.recvline().decode()
#print(z)
m_prime = int(z.split(" ")[-1].strip())
print("m' =", m_prime)

m = (m_prime * inverse(2, n)) % n
print("m =", m)
flag = long_to_bytes(m).decode()
print(flag)

