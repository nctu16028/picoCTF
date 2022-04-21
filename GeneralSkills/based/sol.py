#!/usr/bin/env python3

from pwn import *

ip = "jupiter.challenges.picoctf.org"
port = 29221

context.log_level = "error"
r = remote(ip, port)

def try_bin():
    z = r.recvuntil(b"Please give the ").decode()
    print(z)

    z = r.recvuntil(b" as", drop=True).decode()
    bin_code = z.split(" ")
    print(bin_code)
    bin_ans = ""
    for i in bin_code:
        bin_ans += chr(int(i, 2))
    
    z = r.recvuntil(b"Input:\n").decode()
    print(z)

    print(bin_ans)
    r.sendline(bin_ans.encode())

def try_oct():
    z = r.recvuntil(b"Please give me the  ").decode()
    print(z)

    z = r.recvuntil(b" as", drop=True).decode()
    oct_code = z.split(" ")
    print(oct_code)
    oct_ans = ""
    for i in oct_code:
        oct_ans += chr(int(i, 8))

    z = r.recvuntil(b"Input:\n").decode()
    print(z)

    print(oct_ans)
    r.sendline(oct_ans.encode())

def try_hex():
    z = r.recvuntil(b"Please give me the ").decode()
    print(z)

    hex_code = r.recvuntil(b" as", drop=True).decode()
    print(hex_code)
    hex_ans = bytearray.fromhex(hex_code).decode()

    z = r.recvuntil(b"Input:\n").decode()
    print(z)

    print(hex_ans)
    r.sendline(hex_ans.encode())

try_bin()
try_oct()
try_hex()
z = r.recvline().decode()
print(z)
z = r.recvline().decode()
print(z)

