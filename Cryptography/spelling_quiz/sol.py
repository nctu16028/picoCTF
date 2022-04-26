#!/usr/bin/env python3

with open("public/study-guide.txt") as f:
    words = f.read().split()
tape = "".join(words)

alphabet = list("abcdefghijklmnopqrstuvwxyz")
alpha_freq = [0] * len(alphabet)
freq = dict(zip(alphabet, alpha_freq))
for c in tape:
    freq[c] += 1
print(freq)

freq_order = [k for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
print("Statistical frequency order:\n", freq_order)
real_freq_order = list("eianosrtlcupdmhgkyfvbwxqzj")    # trial and error
print("General frequency order:\n", real_freq_order)
decrypt_dict = dict(zip(freq_order, real_freq_order))

text = open("public/flag.txt", 'r').read()
flag = ''.join([
    decrypt_dict[c]
    if c in decrypt_dict else c
    for c in text
])
print(flag)

