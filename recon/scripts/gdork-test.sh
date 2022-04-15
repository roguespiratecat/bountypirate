#!/bin/bash
echo "[*] Starting Google Dork Testing "
readarray -t array < $3
for e in "${array[@]}"
do
   python3 $1 "$e" > $2
done
   echo "[*] Finished Google Dork Testing results in $2"