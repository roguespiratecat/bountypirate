#!/usr/bin/python3
import pyfiglet
from rich import print

import os
import argparse

license = """
Copyright 2022 Benjamin Keil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

homedir = os.getcwd()

banner = pyfiglet.figlet_format('Bounty Pirate', font='slant')
subText = "Lazy Bounty Hunting & Penetration Testing Framework For well.. Lazy People :-)"
print(f'\n[yellow]{banner}[/yellow]')
print(f'[green]{subText}[/green]')
print(f'[magenta]{license}[/magenta]\n')

parser = argparse.ArgumentParser(description='Simple Pentesting and Enumeration Framework')
parser.add_argument('-r', '--recon', help='Starts a Recon process & workspace set up', action="store_true")
parser.add_argument('-e', '--exploits', help='Generates a exploit workspace ', action="store_true")
parser.add_argument('-v', '--vulners', help='Generates a Vulnerabilty Scanning work space', action="store_true")
parser.add_argument('-d', '--domain', help='Your target Domain', type=str)
parser.add_argument('-w', '--word-list', help='Optional Word List that you may want to use', type=str)

args = parser.parse_args()

if (args.recon is False and args.exploits is False or args.vulners is False) and args.domain is None:
    print("[!] Missing required Inputs!")
    print("[!] Usage : python3  bountyPirate.py -r    -d myDomain.com ")
    print("[!] Usage : python3  bountyPirate.py -v    -d myDomain.com ")
    print("[!] Usage : python3  bountyPirate.py -e    -d myDomain.com ")
    print("[!] Usage : python3  bountyPirate.py -r    -d myDomain.com -w path/to/some/wordlist")
    print("[!] Usage : python3  bountyPirate.py -v -d myDomain.com -w path/to/some/wordlist")

else:
    if args.recon is True:
        hasNoWordList = (args.word_list is None)
        command = f"./recon/setup.sh {args.domain} " if hasNoWordList else f"./recon/setup.sh {args.domain} {args.word_list}"
        os.system(command)
    if args.exploits is True:
        command = f"./exploitation/setup.sh {args.domain} "
        os.system(command)
    if args.vulners is True:
        command = f"./vulnerscan/setup.sh {args.domain} "
        os.system(command)
