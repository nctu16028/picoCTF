#!/usr/bin/env python3

from pwn import *

ip = "mercury.picoctf.net"
port = 11188

context.log_level = "error"
r = remote(ip, port)

z = r.recvuntil(b"flag!\n").decode()
print(z)
flag_en = r.recvline().decode().strip()
print(flag_en)

z = r.recvuntil(b"encrypt? ").decode()
print(z)
key_exposer = "\0" * (50000 - len(flag_en) // 2)    # Let the key position move back to 0 (since the length of keypad is 50000)
r.sendline(key_exposer.encode())

z = r.recvuntil(b"encrypt? ").decode()
#print(z)
key_exposer = "\0" * (len(flag_en) // 2)    # Use 0-bitstream to expose the key stream applied on the flag
r.sendline(key_exposer.encode())
z = r.recvline().decode()
print(z)
flag_key = r.recvline().decode().strip()
print(flag_key)

flag = ""
for i in range(len(flag_en) // 2):
    en_ch_hex = flag_en[2*i: 2*i+2]
    key_ch_hex = flag_key[2*i: 2*i+2]
    #flag_ch = "{:02x}".format(int(en_ch_hex, 16) ^ int(key_ch_hex, 16))
    flag_ch = chr(int(en_ch_hex, 16) ^ int(key_ch_hex, 16))
    flag += flag_ch
print("picoCTF{%s}" % flag)

