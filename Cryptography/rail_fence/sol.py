#!/usr/bin/env python3

with open("message.txt", "r") as f:
    ciphertext = f.read()
print(ciphertext)

#==========================================================#
# x     x     x     x     x     x     x     x     x     x  #
#==========================================================#
#  x   x x   x x   x x   x x   x x   x x   x x   x x   x x #
#==========================================================#
#   x x   x x   x x   x x   x x   x x   x x   x x   x x    #
#==========================================================#
#    x     x     x     x     x     x     x     x     x     #
#==========================================================#
fence = [[False for j in range(len(ciphertext))] for i in range(4)]
sign = -1
curr_row = 0
for col in range(len(ciphertext)):
    fence[curr_row][col] = True
    if curr_row == 0 or curr_row == 3:
        sign = -sign
    curr_row += sign

# Fill the ciphertext in the x's
ptr = 0
for i in range(4):
    for j in range(len(ciphertext)):
        if fence[i][j] == True:
            fence[i][j] = ciphertext[ptr]
            ptr += 1

# Read the text in the right order
flag = ""
sign = -1
curr_row = 0
for col in range(len(ciphertext)):
    flag += fence[curr_row][col]
    if curr_row == 0 or curr_row == 3:
        sign = -sign
    curr_row += sign
print(flag)

