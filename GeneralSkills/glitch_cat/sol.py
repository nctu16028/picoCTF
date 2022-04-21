#!/usr/bin/env python3

from pwn import *

ip = "saturn.picoctf.net"
port = 53933

context.log_level = "error"
r = remote(ip, port)

z = r.recvuntil(b"'}'").decode()    # if using recvall(), '\r' would be read and the text becomes invisible after decoding
print(z)

segments = z.split(" + ")
print(segments)

flag = ""
for s in segments:
    if s[0] == "'":
        flag += s.strip("'")
    else:
        cmd = "flag += " + s
        exec(cmd)
print(flag)

