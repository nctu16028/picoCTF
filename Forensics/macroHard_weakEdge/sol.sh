#!/bin/sh

unzip 'Forensics is fun.pptm' > /dev/null
cat ppt/slideMasters/hidden | tr -d ' ' | base64 -d
rm -rf docProps/ ppt/ _rels/ '[Content_Types].xml' 

