#!/usr/bin/env python3

with open("message.txt", "r") as f:
    ciphertext = f.read()

alphabet = list("abcdefghijklmnopqrstuvwxyz")
alpha_freq = [0] * len(alphabet)
freq = dict(zip(alphabet, alpha_freq))
for c in ciphertext:
    if c.lower() in alphabet:
        freq[c.lower()] += 1
print(freq)

freq_order = [k for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
freq_order_with_cap = []
for k in freq_order:
    freq_order_with_cap.append(k.upper())
    freq_order_with_cap.append(k)
print("Statistical frequency order:\n", freq_order_with_cap)
real_freq_order = list("EeTtIiOoNnSsAaCcRrHhLlUuFfMmDdPpGgVvYyBbKkWwXxQqZzJj")    # trial and error
print("General frequency order:\n", real_freq_order)
decrypt_dict = dict(zip(freq_order_with_cap, real_freq_order))

flag = ''.join([
    decrypt_dict[c]
    if c in decrypt_dict else c
    for c in ciphertext
])
print(flag)

