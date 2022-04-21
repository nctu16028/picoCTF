#!/usr/bin/env python3

from pwn import *
import hashlib

ip = "saturn.picoctf.net"
port = 63116

context.log_level = "error"
r = remote(ip, port)

def one_try():
    z = r.recvuntil(b"\r", drop=True).decode()
    print(z)

    token = z.split(": ")[1].strip("'")
    print(token)

    hash_val = hashlib.md5(token.encode('utf-8')).hexdigest()
    print(hash_val)

    z = r.recvuntil(b'Answer: \r\n')
    print(z)

    r.sendline(hash_val.encode())
    z = r.recvuntil(b'Correct.\r\n')
    print(z)

one_try()
one_try()
one_try()
z = r.recvline()
print(z)

