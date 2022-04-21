import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag_en = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
key = "g"   # <- trial and error (from 'a' to 'p')
assert all([k in ALPHABET for k in key])
assert len(key) == 1

#b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(flag_en):
    enc += shift(c, key[i % len(key)])
print(enc)


def b16_decode(cipher):
    dec = ""
    for i in range(len(cipher) // 2):
        bin1 = "{0:04b}".format(ord(cipher[2*i]) - LOWERCASE_OFFSET)
        bin2 = "{0:04b}".format(ord(cipher[2*i+1]) - LOWERCASE_OFFSET)
        binary = bin1 + bin2
        dec += chr(int(binary, 2))
    return dec

flag = b16_decode(enc)
print(flag)
