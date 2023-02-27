#!/bin/sh

tshark -nr shark2.pcapng -Y 'dns && ip.dst == 18.217.1.57' | awk '{ print $12 }' | awk -F. '{ print $1 }' | uniq | tr -d '\n' | base64 -d
echo

