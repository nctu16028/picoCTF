#!/usr/bin/env python3

from pwn import *

ip = "mercury.picoctf.net"
port = 49039

context.log_level = "error"
r = remote(ip, port)

z = r.recvall().split(b" \n")[:-1]
f = [chr(int(byte)) for byte in z]  # chr(): int to ascii
flag = "".join(f)
print(flag)

