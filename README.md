# bountypirate

![./assets](img.png)

**Note Python3 is required!**



## Installing requirements


``bash
pip install -r requirements.txt
``

## What am I looking at?

Bounty pirate is a Penetration Testing Framework For well.. Lazy People :-)
I wrote this little framework mainly because I have a short term memory 
and could not keep up with all the commands that I needed to remember for scanning and exploit
tools like nmap, wfuzz, amass etc. So This little script takes care of that for me, by executing these commands for me.




## Quick Usage

````txt
python3 bountypirate.py [-h] [-r] [-e] [-v] [-d DOMAIN] [-w WORD_LIST]


    ____                    __           ____  _            __
   / __ )____  __  ______  / /___  __   / __ \(_)________ _/ /____
  / __  / __ \/ / / / __ \/ __/ / / /  / /_/ / / ___/ __ `/ __/ _ \
 / /_/ / /_/ / /_/ / / / / /_/ /_/ /  / ____/ / /  / /_/ / /_/  __/
/_____/\____/\__,_/_/ /_/\__/\__, /  /_/   /_/_/   \__,_/\__/\___/
                            /____/

Lazy Bounty Hunting & Penetration Testing Framework For well.. Lazy People :-)

Copyright 2022 Benjamin Keil

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Simple Pentesting and Enumeration Framework

optional arguments:
  -h, --help            show this help message and exit
  -r, --recon           Starts a Recon process & workspace set up
  -e, --exploits        Generates a exploit workspace
  -v, --vulners         Generates a Vulnerabilty Scanning work space
  -d DOMAIN, --domain DOMAIN
                        Your target Domain
  -w WORD_LIST, --word-list WORD_LIST
                        Optional Word List that you may want to use
````

## Getting Started

A good work flow is to identify your target domain lets say 
``https://myVulnerableDomain.com``

Now bountypirate can help you to create a works space and directory hierarchy to start you normal penetration testing and recon process.

````commandline
python3 bountiprate.py -r -v -e -d myVulnerableDomain.com
````

This will create a new work space in ``$HOME/bounty_pirate/myVulnerableDomain.com``
Also it will start a few recon scripts like nmap, amass and generate a few Github & google dorks for
to do some initial recon on your target.

Inside ``$HOME/bounty_pirate/myVulnerableDomain.com``  you will find 3 Directories

1. recon
2. exploitation
3. vulnerscan

Each directory has a bunch of scripts and one python file that will execute desired tools/scrips

### recon-manage.py
````commandline
usage: python3 recon-manager.py [-h] [-s] [-c] [-l] [-a] [-m] [-g] [-ps] [-d] [-i] [-up] [-w WORD_LIST] [-r] [-ss]

Simple Pentesting and Enumeration Framework

optional arguments:
  -h, --help            show this help message and exit
  -s, --server          Starts a Simple Server on port: 9393
  -c, --content-discovery
                        Start Simple Content Discovery
  -l, --amass-list      Shows all Amass Enumerations
  -a, --amass-show      Displays Amass Enumeration Result
  -m, --mass-scan       Starts a Mass Scan on subdomains
  -g, --google-dork-test
                        Runs Google Dork Queries on Domain(s)
  -ps, --probe-server   probes all subdomains
  -d, --directory-search
                        starts gobuster scan
  -i, --screen-shots    generates web screen shots
  -up, --use-proxy      weather to use Proxy Chains (TOR needs to be running!)
  -w WORD_LIST, --word-list WORD_LIST
                        word list to use
  -r, --random-agent    use random useragent
  -ss, --ssl            use ssl
````

### vulners-manager.py
````commandline
usage: python3 vulners-manager.py [-h] [-nk] [-sf] [-us] [-ws] [-ar] [-sm] [-nm] [-gb] [-fb] [-wf] [-pr] [-ssl] [-s]

Simple Pentesting and Enumeration Framework

optional arguments:
  -h, --help          show this help message and exit
  -nk, --nikto        Starts a Nikto scan
  -sf, --skipfish     start skipfish
  -us, --uniscan      start uniscan
  -ws, --wpscan       start wpcan
  -ar, --arjun        Run Arjun API enumerator
  -sm, --sqlmap       Run sqlmap on target
  -nm, --nmap         probes all subdaims
  -gb, --gobuster     starts gobuster
  -fb, --feroxbuster  starts ferosbuster
  -wf, --wfuzz        starts wfuzz
  -pr, --use-proxy    use proxychains
  -ssl, --use-ssl     use ssl
  -s, --start-server  Starts a Simple Server for Directory Browsing on port 9393
````


