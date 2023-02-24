#!/bin/sh

unzip files.zip > /dev/null
find files/ -type f -name "uber-secret.txt" -exec cat {} \;
rm -rf files/

