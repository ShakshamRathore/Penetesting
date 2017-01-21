#!/usr/bin/env python3
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
__credits__ = ["maldevel", "nma-io"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "maldevel"

################################

import argparse
import sys
import os
import requests

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

################################

def _analyzeHost(host, proxies):
  try:
    data = requests.get(host, verify=False, proxies=proxies)
  except requests.exceptions.ConnectionError as e:
    print red('[-] {}: Connection Error ({})'.format(host, e))
    return None

  if data.status_code not in range(200, 209):
    print red('[-] {}: Status code {}'.format(host, data.status_code))
    return None

  print green('[+] {}: {} {}'.format(host, data.status_code, requests.status_codes._codes[data.status_code][0].upper()))

  headers = data.headers

  return headers

################################

def _checkHeaders(headers, https=False):
  results = []

  secureHeaders = {
    'X-Frame-Options':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#X-Frame-Options',
    'X-XSS-Protection':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#X-XSS-Protection',
    'X-Content-Type-Options':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#X-Content-Type-Options',
    'Content-Security-Policy':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#Content-Security-Policy',
    'X-Permitted-Cross-Domain-Policies':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#X-Permitted-Cross-Domain-Policies'
  }

  if https:
    secureHeaders.update({
      'Strict-Transport-Security':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#HTTP_Strict_Transport_Security_.28HSTS.29',
      'Public-Key-Pins':'https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#Public_Key_Pinning_Extension_for_HTTP_.28HPKP.29'
    })

  for h in list(secureHeaders):
    if h not in headers:
      results.append('{}: {}'.format(h, secureHeaders[h]))

  return results

################################

message = """
 _____                            _   _                _               
/  ___|                          | | | |              | |              
\ `--.  ___  ___ _   _ _ __ ___  | |_| | ___  __ _  __| | ___ _ __ ___ 
 `--. \/ _ \/ __| | | | '__/ _ \ |  _  |/ _ \/ _` |/ _` |/ _ \ '__/ __|
/\__/ /  __/ (__| |_| | | |  __/ | | | |  __/ (_| | (_| |  __/ |  \__ \\
\____/ \___|\___|\__,_|_|  \___| \_| |_/\___|\__,_|\__,_|\___|_|  |__ /
                      
               OWASP Secure Headers Checker | @maldevel                
                             {}: {}
""".format(red('Version'), yellow(__version__)) 

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description=message, formatter_class=RawTextHelpFormatter)

  parser.add_argument("-H", "--host", 
                        action="store", 
                        metavar='hostname',
                        dest='host', 
                        type=str, 
                        default=None, 
                        required=True, 
                        help='The host to check, e.g. http://example.com, https://example.com, http://192.168.1.1')

  parser.add_argument('-x', '--proxy', 
                        action="store", 
                        metavar='PROXY', 
                        dest='proxy', 
                        type=str,
                        default=None, 
                        required=False, 
                        help='Use proxy (eg. http://127.0.0.1:8080).')

  if len(sys.argv) is 1:
    parser.print_help()
    sys.exit(1)

  args = parser.parse_args()
  
  print message

  host = args.host   
  https = False

  if '://' not in host:
    print red('[-] {}: Invalid host'.format(host))
    sys.exit(2) 

  proxies = {
      'http': args.proxy,
      'https': args.proxy,
  }

  if 'https' in host:
    https = True

  results = _analyzeHost(host, proxies)
  if not results:
    print red('[-] {}: An error occured during host analysis'.format(host))
    sys.exit(3)
  
  print green('[+] {}: Checking headers'.format(host))

  headers = results

  http_headers_vulns = _checkHeaders(headers)
  if not http_headers_vulns:
    print red('[-] {}: An error occured during host analysis'.format(host))
    sys.exit(4)

  print green('[+] {}: Missing OWASP Secure Headers:'.format(host))
  print '\t* {}'.format('\n\t* '.join(http_headers_vulns))
  
  print green('[+] {}: Finish'.format(host))
  print ''

