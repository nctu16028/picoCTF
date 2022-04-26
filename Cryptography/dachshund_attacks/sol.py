#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
from pwn import *
from math import sqrt, floor
from continued_fractions import *

ip = "mercury.picoctf.net"
port = 37455

context.log_level = "error"
r = remote(ip, port)

z = r.recvuntil(b"e: ").decode()
print(z)
e = int(r.recvuntil(b"\nn: ", drop=True).decode())
print("e =", e)
n = int(r.recvuntil(b"\nc: ", drop=True).decode())
print("n =", n)
c = int(r.recvuntil(b"\n", drop=True).decode())
print("c =", c)

# The following applys Wiener's attack (Reference: https://en.wikipedia.org/wiki/Wiener%27s_attack)
cont_fracs = rational_to_contfrac(e, n)
convergents = convergents_from_contfrac(cont_fracs)
for (k, d) in convergents:
    if k != 0 and e*d % k == 1:
        phi_n = e * d // k
        sum_of_p_and_q = n + 1 - phi_n

        # Check whether x^2 - (sum_of_p_and_q)*x + n = 0 has integer roots (p and q)
        det = sum_of_p_and_q ** 2 - 4 * 1 * n   # D = b^2 - 4ac
        if det >= 0:
            #sq = floor(sqrt(det))
            sq = int_sqrt(det)
            if sq * sq == det and (sq + sum_of_p_and_q) % 2 == 0:   # sqrt(D) is integer and (-b+-sqrt(d))/2 are integers
                print("d =", d)
                break

m = pow(c, d, n)
print("m =", m)
flag = long_to_bytes(m).decode()
print(flag)

