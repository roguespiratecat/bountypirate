#!/bin/bash
echo "[*] Probing active Web responses on subdomains"
cat $1 | httprobe > $2
cat $2