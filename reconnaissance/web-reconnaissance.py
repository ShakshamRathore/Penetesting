#!/usr/bin/python
# encoding: UTF-8

"""
    This file is part of PenTestKit
    Copyright (C) 2017 @maldevel
    https://github.com/maldevel/PenTestKit
    
    PenTestKit - Useful tools for Penetration Testing.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.

"""

__author__ = "maldevel"
__copyright__ = "Copyright (c) 2017 @maldevel"
__credits__ = ["maldevel"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "maldevel"

################################

import argparse
import sys
import os
import requests

from bs4 import BeautifulSoup, Comment
from termcolor import colored
from argparse import RawTextHelpFormatter

################################

from requests.packages.urllib3.exceptions import InsecureRequestWarning #remove insecure https warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #remove insecure https warning

################################
    
def yellow(text):
    return colored(text, 'yellow', attrs=['bold'])

def green(text):
    return colored(text, 'green', attrs=['bold'])

def red(text):
    return colored(text, 'red', attrs=['bold'])

def cyan(text):
    return colored(text, 'cyan', attrs=['bold'])

def magenta(text):
    return colored(text, 'magenta', attrs=['bold'])
    
def blue(text):
    return colored(text, 'blue', attrs=['bold'])
    
################################

message = """
 __          __  _     _____                      
 \ \        / / | |   |  __ \                     
  \ \  /\  / /__| |__ | |__) |___  ___ ___  _ __  
   \ \/  \/ / _ \ '_ \|  _  // _ \/ __/ _ \| '_ \ 
    \  /\  /  __/ |_) | | \ \  __/ (_| (_) | | | |
     \/  \/ \___|_.__/|_|  \_\___|\___\___/|_| |_|
                                                  
       Web Application Reconnaissance | @maldevel                
                                     {}: {}
""".format(blue('Version'), green(__version__)) 


def parseArgs():
    parser = argparse.ArgumentParser(description=message, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-u", "--url", action="store", metavar='URL', dest='url', type=str,
                        default=None, required=True,
                        help='The url to scan, e.g. http://example.com, https://example.com, http://192.168.1.1')
    parser.add_argument('-o', '--output', action='store', metavar='LOGFILE', dest='logs', type=str, default=None,
                        help='Log file path')
    args = parser.parse_args()
    
    return args


def find_headers(url, logfile):
    r = requests.head(url, verify=False)
    
    print magenta('[+] Headers')
    if logfile:
        logfile.write('### Headers\n\n')
        
    for key, value in r.headers.items() :
        print '{} {}: {}'.format(green('>'), key, value)
        if logfile:
            logfile.write('* {}: {}\n'.format(key, value))
    
    
def find_meta(url, logfile):
    html = requests.get(url, verify=False).content
    soup = BeautifulSoup(html, 'lxml') #html5lib
    
    print magenta('[+] Meta tags')
    if logfile:
        logfile.write('### Meta tags\n\n')

    for tag in soup.find_all('meta'):
        print '{} {}'.format(green('>'), tag)
        if logfile:
            logfile.write('```html\n{}\n```\n\n'.format(tag))


def find_comments(url, logfile):
    html = requests.get(url, verify=False).content
    soup = BeautifulSoup(html, 'lxml') #html5lib
    
    print magenta('[+] HTML Comments')
    if logfile:
        logfile.write('### HTML Comments\n\n')
        
    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
        print '{} {}'.format(green('>'), comment)
        if logfile:
            logfile.write('```html\n{}\n```\n\n'.format(comment))
    

if __name__ == '__main__':

    args = parseArgs()
    print message

    url = args.url
    logs = False
    
    if args.logs:
        filepath = args.logs
        if not filepath.endswith('.md'):
            filepath = filepath + '.md'
        logs = open(filepath, 'w')
        
    if '://' not in url:
        print red('[-] {}: Invalid url'.format(url))
        sys.exit(1) 
    
    if logs:
        logs.write('## Web Application Reconnaissance\n')
        logs.write('\n***\n')
        logs.write('\n')
        
    find_headers(url, logs)
    print ''
    if logs:
        logs.write('\n***\n\n')
        
    find_meta(url, logs)
    print ''
    if logs:
        logs.write('***\n\n')
        
    find_comments(url, logs)
    print ''
    if logs:
        logs.write('***\n\n')
        
        
        
        
