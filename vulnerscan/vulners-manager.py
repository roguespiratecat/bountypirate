#!/usr/bin/python3
import pyfiglet
from rich import print

import os
import argparse

domain="DOMAIN"

license="""
Copyright 2022 Benjamin Keil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


homedir =os.getcwd()

banner = pyfiglet.figlet_format('Vulners Scanner & Manager', font='slant')
subText="Lazy Bounty Hunting & Penetration Testing Framework For well.. Lazy People :-)"
print(f'\n[yellow]{banner}[/yellow]')
print(f'[green]{subText}[/green]')
print(f'[magenta]{license}[/magenta]\n')



parser = argparse.ArgumentParser(description='Simple Pentesting and Enumeration Framework')
parser.add_argument('-nk','--nikto',              help='Starts a Nikto scan',action="store_true")
parser.add_argument('-sf','--skipfish',           help='start skipfish',action="store_true")
parser.add_argument('-us','--uniscan',            help='start uniscan',action="store_true")
parser.add_argument('-ws','--wpscan',             help='start wpcan',action="store_true")
parser.add_argument('-ar','--arjun',              help='Run Arjun API enumerator',action="store_true")
parser.add_argument('-sm','--sqlmap',             help='Run sqlmap on target',action="store_true")
parser.add_argument('-nm','--nmap',               help='probes all subdaims',action="store_true")
parser.add_argument('-gb','--gobuster',           help='starts gobuster',action="store_true")
parser.add_argument('-fb','--feroxbuster',        help='starts ferosbuster',action="store_true")
parser.add_argument('-wf','--wfuzz',              help='starts wfuzz',action="store_true")
parser.add_argument('-pr','--use-proxy',          help='use proxychains',action="store_true")
parser.add_argument('-ssl','--use-ssl',           help='use ssl',action="store_true")
parser.add_argument('-s','--start-server',        help='Starts a Simple Server for Directory Browsing on port 9393',action="store_true")



args = parser.parse_args()

if (args.start_server = False and args.nikto == False and args.skipfish == False  and args.uniscan == False and args.wpscan == False and args.arjun == False and args.sqlmap == False and args.nmap == False and args.gobuster == False and args.feroxbuster == False and args.wfuzz == False ):
	print("[!] Missing required Inputs ")
	print("[!] Usage : python3  recon-manager.py --nikto   ")
	print("[!] Usage : python3  recon-manager.py --skipfish")
	print("[!] Usage : python3  recon-manager.py --uniscan   ")
	print("[!] Usage : python3  recon-manager.py --wpscan ")
	print("[!] Usage : python3  recon-manager.py --arjun   ")
	print("[!] Usage : python3  recon-manager.py --sqlmap ")
	print("[!] Usage : python3  recon-manager.py --nmap   ")
	print("[!] Usage : python3  recon-manager.py --gobuster")
	print("[!] Usage : python3  recon-manager.py --feroxbuster")
	print("[!] Usage : python3  recon-manager.py --wfuzz")
else:
	protocol = "https://" if args.use_ssl else "http://"
	proxy = "proxychains4 -q " if args.use_ssl else ""
	if args.start_server == True
		os.system("python3 -m http.server 9393")
		exit(0)
	if args.nikto == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/nikto/nikto.log"
		os.system(command)
		command = f"{proxy} nikto -h {protocol}{domain} -output {outfile}"
		os.system(command)
		exit(0)
	if args.skipfish == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/skipfish/skipfish.log"
		command = f"{proxy} skipfish -o {outfile} {protocol}{domain}"
		os.system(command)
		exit(0)
	if args.uniscan == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/uniscan/uniscan.log"
		command = f"{proxy} uniscan -u {protocol}{domain} -qweds"
		os.system(command)
		exit(0)
	if args.wpscan == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/wpscan/wpscan.log"
		command = f"{proxy} wpscan --url {protocol}{domain} -o {outfile}"
		os.system(command)
		exit(0)
	if args.arjun == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/arjun/arjun.txt"
		command = f"{proxy} arjun -u  {protocol}{domain} -oT {outfile}"
		os.system(command)
		exit(0)
	if args.sqlmap == True:
		print("[!] Ambigious command printing help instead")
		os.system("sqlmap -h")
		exit(0)
	if args.nmap == True:
		dir_path = os.path.dirname(os.path.realpath(__file__))
		outfile =f"{dir_path}/nmap/initial.log"
		os.system(f"nmap -sV -sC -oN {outfile} {domain}")
		exit(0)
	if args.gobuster == True:
		wl= "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt"
		os.system(f"gobuster dir -u {protocol}{domain} -w {wl}")
		exit(0)
	if args.feroxbuster == True:
		##feroxbuster -u http://127.1 -x pdf -x js,html -x php txt json,docx
		dir_path = os.path.dirname(os.path.realpath(__file__))
		wl= "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt"
		outfile =f"{dir_path}/feroxbuster/scan.log"
		command = f"{proxy} feroxbuster -u {protocol}{domain} -w {wl} -x pdf -x js,html -x php txt json,docx,bak,env,cgi -o outfile"
		os.system(command)
	if args.wfuzz == True:
		print("[!] Ambigious command printing help instead")
		print("[!] Example Command: \nwfuzz -z file,wordlist/others/common_pass.txt -d 'uname=FUZZ&pass=FUZZ'  --hc 302 http://testphp.vulnweb.com/userinfo.php")
		print(f"[!] Example Command: \nwfuzz -z file,wordlist/others/common_pass.txt -d 'uname=FUZZ&pass=FUZZ'  --hc 302 {domain}")
		print("[!] Available Word List Directories")
		os.system("ls -r /usr/share/wfuzz/wordlist/*")
		
