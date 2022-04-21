lst = ["01101101", "01100001", "01110000"]
bin_ans = ""
for i in lst:
    bin_ans += chr(int(i, 2))
print(bin_ans)

lst = ["146", "141", "154", "143", "157", "156"]
oct_ans = ""
for i in lst:
    oct_ans += chr(int(i, 8))
print(oct_ans)

hex_str = "7375626d6172696e65"
hex_ans = bytearray.fromhex(hex_str).decode()
print(hex_ans)

