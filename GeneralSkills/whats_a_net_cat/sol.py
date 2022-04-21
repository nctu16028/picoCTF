#!/usr/bin/env python3

from pwn import *

ip = "jupiter.challenges.picoctf.org"
port = 64287

context.log_level = "error"
r = remote(ip, port)
r.interactive()

