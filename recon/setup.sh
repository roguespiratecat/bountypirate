#!/bin/bash

currentDir=$(pwd)/recon
workspace=$HOME/bounty_pirate
wordList=$2
projectDir=$1
outdir=recon

if [ -d "$workspace" ] ; then  
	echo "[*]  Bounty Pirate Workspace Exists Skiping directory setup"
else
	echo "[*] Bounty Pirate Workspace not found, Initializing Bounty Pirate Workspace at $workspace"
	mkdir $workspace
fi

if [ -d "$workspace/$projectDir/$outdir" ] ; then  
    echo "[*] workspace context allready exists !"
    echo "[*] Please cd into $workspace/$projectDir/$outdir recon-manager.py"
    exit 0
fi

if [ -d "$workspace/$projectDir/" ] ; then  
    echo "[*] Project context allready exists at $workspace/$projectDir!"
else
    echo "[*] Project context $workspace/$projectDir not found creating it"
    mkdir $workspace/$projectDir
fi
mkdir $workspace/$projectDir/$outdir/



echo "[*] Creating new Recon Workspace at $workspace/$projectDir/$outdir"

mkdir $workspace/$projectDir/$outdir/content-discovery
mkdir $workspace/$projectDir/$outdir/screenshots
mkdir $workspace/$projectDir/$outdir/dorking
mkdir $workspace/$projectDir/$outdir/nmap
mkdir $workspace/$projectDir/$outdir/tools

if [ -z $wordList ] ; then
    echo '[*] No wordlist provided using default :\n/usr/share/amass/wordlists/deepmagic.com_top50kprefixes.txt '
    wordList=/usr/share/amass/wordlists/deepmagic.com_top50kprefixes.txt
fi
echo ""
echo "[*] Generating Github Dorks"
echo ""

$currentDir/scripts/githubDorks.sh $1 > $workspace/$projectDir/$outdir/dorking/$1_githubDorks.txt

echo ""
echo "[*]  Github Dorks generated do you want to write them out to console y/n?"
while true; do
    read -p "Github Dorks generated Do you want to print them to Console?" yn
    case $yn in
        [Yy]* ) cat $workspace/$projectDir/$outdir/dorking/$1_githubDorks.txt; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo ""
echo ""
echo "[*] Generating Google Dorks for Domain $1"
echo ""
python3 $currentDir/scripts/parseDorks.py > tmp.txt
awk '{sub(/REPLACE_ME/,"'$1'")}1' tmp.txt > $workspace/$projectDir/$outdir/dorking/$1_googleDorks.txt
rm tmp.txt

echo "[*] Starting Initial Nmap Scan"
echo ""
ip=$(dig +short $1)
nmap -sC -sV -oN $workspace/$projectDir/$outdir/nmap/$1_nmapscan.txt $ip

echo "[*] Starting Amass Enumeration That may take a while"
echo ""
amass enum -active -d $1  -brute -w  $wordList  -dir $workspace/$projectDir/$outdir/amass_$1_db -o $workspace/$projectDir/$outdir/amass_$1.txt
echo ""
echo "[*] Finalizing Recon Setup"


echo "[*] Finalizing Recon Setup"

awk '{sub(/DOMAIN/,"'$1'")}1' $currentDir/recon-manager.py > $workspace/$projectDir/$outdir/recon-manager.py
cp -r $currentDir/scripts/* $workspace/$projectDir/$outdir/tools
echo "[*] Recon Initial Setup Finished"
