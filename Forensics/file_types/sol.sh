#!/bin/sh

rm -rf flag*

./Flag.pdf
ar -p flag > flag1
cpio -i < flag1
bzip2 -d flag
mv flag.out flag.gz
gzip -d flag.gz
lzip -d flag
lz4 -d flag.out flag
mv flag flag.xz
lzma -d flag.xz
lzop -d -o flag2 flag
lzip -d flag2
mv flag2.out flag2.xz
xz -d flag2.xz
cat flag2 | xxd -p -r
