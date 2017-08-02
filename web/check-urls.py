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

import requests
import sys
import os
import argparse
from argparse import RawTextHelpFormatter

################################

def check_url(url, logfile):
    try:
        r = requests.head(url)
        print("HEAD: {}: {}".format(url, r.status_code))
        logfile.write('HEAD;{};{}\n'.format(url, r.status_code))
    except Exception as ex:
        print("HEAD {}: request failed..".format(url))
        logfile.write('HEAD;{};request failed\n'.format(url))
        
    try:
        r = requests.get(url)
        print("GET: {}: {}".format(url, r.status_code))
        logfile.write('GET;{};{}\n'.format(url, r.status_code))
    except Exception as ex:
        print("GET {}: request failed..".format(url))
        logfile.write('GET;{};request failed\n'.format(url))
        
    try:
        r = requests.post(url)
        print("POST: {}: {}".format(url, r.status_code))
        logfile.write('POST;{};{}\n'.format(url, r.status_code))
    except Exception as ex:
        print("POST {}: request failed..".format(url))
        logfile.write('POST;{};request failed\n'.format(url))
          
def check_file_urls(filename, logfile):

    logfile.write('METHOD;URL;STATUS\n')
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            if line:
            
                url1 = "http://{}".format(line)
                url2 = "https://{}".format(line)
                
                check_url(url1, logfile)
                check_url(url2, logfile)
                    
                print ''
                
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='{}'.format('Get HTTP response status code for a list of URLs.'), formatter_class=RawTextHelpFormatter)

    parser.add_argument("-f", "--filename", action="store", metavar='FILE', dest='filename',  type=str, default=None, required=True, help='File containing urls.')
    parser.add_argument("-o", "--output", action="store", metavar='FILE', dest='outputFile', type=str, default='results.csv', required=False, help='File to write results.')

    if len(sys.argv) is 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()

    print '\n[*] Get HTTP response status code for a list of URLs.'
    
    if (not os.path.isfile(args.filename)):
        print '[-] Please provide an existing file.\n'
        sys.exit()
        
    try:
        with open(args.outputFile, 'w') as logfile:
            print '\nchecking urls from file {}..\n'.format(args.filename)
            check_file_urls(args.filename, logfile)
        
    except KeyboardInterrupt:
        sys.exit(0)

