#!/bin/bash

currentDir=$(pwd)/vulnerscan
workspace=$HOME/bounty_pirate
wordList=$2
projectDir=$1
outdir=vulners

if [ -d "$workspace" ] ; then  
	echo "[*]  Bounty Pirate Workspace Exists Skiping directory setup"
else
	echo "[*] Bounty Pirate Workspace not found, Initializing Bounty Pirate Workspace at $workspace"
	mkdir $workspace
fi

if [ -d "$workspace/$projectDir/$outdir" ] ; then  
    echo "[*] workspace context allready exists !"
    echo "[*] Please cd into $workspace/$projectDir/$outdir and run python3 vulners-manager.py"
    exit 0
fi

if [ -d "$workspace/$projectDir/" ] ; then  
    echo "[*] Project context allready exists at $workspace/$projectDir!"
else
    echo "[*] Project context $workspace/$projectDir not found creating it"
    mkdir $workspace/$projectDir
fi
mkdir $workspace/$projectDir/$outdir/




echo "[*] Creating new Vulners Workspace at $workspace/$projectDir/$outdir"


mkdir $workspace/$projectDir/$outdir/nikto
mkdir $workspace/$projectDir/$outdir/skipfish
mkdir $workspace/$projectDir/$outdir/uniScan
mkdir $workspace/$projectDir/$outdir/wpscan
mkdir $workspace/$projectDir/$outdir/wfuzz
mkdir $workspace/$projectDir/$outdir/arjun
mkdir $workspace/$projectDir/$outdir/sqlmap
mkdir $workspace/$projectDir/$outdir/nmap
mkdir $workspace/$projectDir/$outdir/gobuster
mkdir $workspace/$projectDir/$outdir/feroxbuster


echo "[*] Finalizing Vulners Setup"

awk '{sub(/DOMAIN/,"'$1'")}1' $currentDir/vulners-manager.py > $workspace/$projectDir/$outdir/vulners-manager.py
echo "[*] Vulners Initial Setup Finished"
