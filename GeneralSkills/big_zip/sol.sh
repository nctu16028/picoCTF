#!/bin/sh

unzip big-zip-files.zip > /dev/null
grep -r "picoCTF" big-zip-files/*
rm -rf big-zip-files/

