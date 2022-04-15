#!/usr/bin/python3
import pyfiglet
from rich import print

import os
import argparse

domain = "DOMAIN"

license = """
Copyright 2022 Benjamin Keil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

homedir = os.getcwd()

banner = pyfiglet.figlet_format('Recon Manager', font='slant')
subText = "Lazy Bounty Hunting & Penetration Testing Framework For well.. Lazy People :-)"
print(f'\n[yellow]{banner}[/yellow]')
print(f'[green]{subText}[/green]')
print(f'[magenta]{license}[/magenta]\n')

parser = argparse.ArgumentParser(description='Simple Pentesting and Enumeration Framework')
parser.add_argument('-s', '--server', help='Starts a Simple Server on port: 9393', action='store_true')
parser.add_argument('-c', '--content-discovery', help='Start Simple Content Discovery', action='store_true')
parser.add_argument('-l', '--amass-list', help='Shows all Amass Enumerations', action='store_true')
parser.add_argument('-a', '--amass-show', help='Displays Amass Enumeration Result', action='store_true')
parser.add_argument('-m', '--mass-scan', help='Starts a Mass Scan on subdomains', action='store_true')
parser.add_argument('-g', '--google-dork-test', help='Runs Google Dork Queries on Domain(s)', action='store_true')
parser.add_argument('-ps', '--probe-server', help='probes all subdomains', action='store_true')
parser.add_argument('-d', '--directory-search', help='starts gobuster scan ', action='store_true')
parser.add_argument('-i', '--screen-shots', help='generates web screen shots ', action='store_true')
parser.add_argument('-up', '--use-proxy', help='weather to use Proxy Chains (TOR needs to be running!)',
                    action='store_true')
parser.add_argument('-w', '--word-list', help='word list to use', type=str)
parser.add_argument('-r', '--random-agent', help='use random useragent', action='store_true')
parser.add_argument('-ss', '--ssl', help='use ssl', action='store_true')

args = parser.parse_args()


def check_args( args ):
    return args.server is False and args.content_discovery is False and args.amass_list is False and args.amass_show is False and args.mass_scan is False and args.google_dork_test is False and args.probe_server is False and args.directory_search is False and args.screen_shots


if check_args(args):
    print("[!] Missing required Inputs ")
    print("[!] Usage : python3  recon-manager.py --server   ")
    print("[!] Usage : python3  recon-manager.py --content-discovery")
    print("[!] Usage : python3  recon-manager.py --amass-list   ")
    print("[!] Usage : python3  recon-manager.py --amass-show ")
    print("[!] Usage : python3  recon-manager.py --mass-scan   ")
    print("[!] Usage : python3  recon-manager.py --google-dork-test ")
    print("[!] Usage : python3  recon-manager.py --probe-servers   ")
    print("[!] Usage : python3  recon-manager.py --directory-search")
    print("[!] Usage : python3  recon-manager.py --screen-shots")
else:
    if args.server is True:
        os.system("python3 -m http.server 9393")
        exit(0)
    if args.content_discovery is True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        script_path = f"{dir_path}/tools/content-discovery.sh"
        os.system(f"{script_path} '{dir_path}/amass_{domain}.txt' '{dir_path}/content-discovery'")
    if args.amass_list is True:
        os.system(f"amass db -dir amass_{domain}_db -list")
        print("")
        exit(0)
    if args.amass_show is True:
        os.system(f"amass db -dir amass_{domain}_db -show ")
        print("")
        exit(0)
    if args.mass_scan is True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        script_path = f"{dir_path}/tools/dnmasscan"
        os.system(f"{script_path} {dir_path}/amass_{domain}.txt dns.log -p1-65535 -oG massScan.log")
        exit(0)
    if args.google_dork_test is True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        script_path = f"{dir_path}/tools/gdork-test.sh"
        os.system(
            f"{script_path}  '{dir_path}/tools/degoogle.py' '{dir_path}/dorking/degoogle.txt' '{dir_path}/dorking/{domain}_googleDorks.txt'")
        exit(0)
    if args.probe_server is True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        script_path = f"{dir_path}/tools/httprober.sh"
        os.system(f"{script_path} {dir_path}/amass_{domain}.txt {dir_path}/content-discovery/httprobe.txt")
        exit(0)
    if args.directory_search is True:
        protocol = "https://" if args.ssl else "http://"
        hasNoWordList = (args.word_list is None)
        wl = "/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt" if hasNoWordList else args.word_list
        os.system(f"gobuster dir -u {protocol}{domain} -w {wl}")
        exit(0)
    if args.screen_shots is True:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.system(f"eyewitness -f {dir_path}/amass_{domain}.txt  -d {dir_path}/screenshots")
