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
__credits__ = ["maldevel", "redteamsecurity"]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "maldevel"

################################

import requests
import json
import sys
import argparse
import time

from argparse import RawTextHelpFormatter
from getpass import getpass

################################

from requests.packages.urllib3.exceptions import InsecureRequestWarning #remove insecure https warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #remove insecure https warning

################################

class create_menu:
    def __init__(self, menu, text, other):
        self.text = text
        self.menu = menu
        self.other = other

        # Build the menu
        option_length_menu = len(menu)
        option_length_text = len(text)
        if self.other != 'Null':
            print('%s' + (20-option_length_menu) * ' ' + '  :    %s' + (15-option_length_text)*' ' +  ':    %s') %(menu,text,other)

        else:
            print('%s' + (15-option_length_menu) * ' ' + '  :  %s') %(menu,text)
        return

################################

def build_url(url, resource):
    return '{0}{1}'.format(url, resource)

################################

def connect(method, url, resource, token, data=None, params=None):
    headers = {'X-Cookie': 'token={0}'.format(token), 'content-type': 'application/json'}

    data = json.dumps(data)

    if method == 'POST':
        r = requests.post(build_url(url, resource), data=data, headers=headers, verify=verify)
    elif method == 'PUT':
        r = requests.put(build_url(url, resource), data=data, headers=headers, verify=verify)
    elif method == 'DELETE':
        r = requests.delete(build_url(url, resource), data=data, headers=headers, verify=verify)
    else:
        r = requests.get(build_url(url, resource), params=params, headers=headers, verify=verify)

    if r.status_code != 200:
        e = r.json()
        print e['error']
        sys.exit()

    # When downloading a scan we need the raw contents not the JSON data.
    if 'download' in resource:
        return r.content

    # All other responses should be JSON data. Return raw content if they are
    # not.
    try:
        return r.json()
    except ValueError:
        return r.content

################################

def login(url, usr, pwd):
    login = {'username': usr, 'password': pwd}
    data = connect('POST', url, '/session', '', data=login)
    return data['token']

################################

def get_policies(url, token):
    data = connect('GET', url, '/editor/policy/templates', token)
    return dict((p['title'], p['uuid']) for p in data['templates'])

################################

def get_scans(url, token):
    data = connect('GET', url, '/scans/', token)
    status_dict = dict((p['name'], p['status']) for p in data['scans'])
    id_dict = dict((b['name'], b['id']) for b in data['scans'])

    return status_dict, id_dict

################################

def get_history_ids(url, sid, token):
    data = connect('GET', url, '/scans/{0}'.format(sid), token)
    temp_hist_dict = dict((h['history_id'], h['status']) for h in data['history'])
    temp_hist_dict_rev = {a:b for b,a in temp_hist_dict.items()}
    try:
        for key,value in temp_hist_dict_rev.items():
            print key
            print value
    except:
        pass

################################

def get_scan_history(url, sid, hid, token):
    params = {'history_id': hid}
    data = connect('GET', url, '/scans/{0}'.format(sid), token, params)
    return data['info']

################################

def get_status(sid, url, token):
    time.sleep(3) # sleep to allow nessus to process the previous status change
    temp_status_dict, temp_id_dict = get_scans(url, token)
    print '\nScan Name           Status  '
    print '---------------------------------------'
    for key, value in temp_id_dict.items():
        if str(value) == str(sid):
            create_menu(key, temp_status_dict[key], 'Null')

################################

def launch(url, sid, token):
    data = connect('POST', url, '/scans/{0}/launch'.format(sid), token)
    return data['scan_uuid']

################################

def pause(url, sid, token):
    connect('POST', url, '/scans/{0}/pause'.format(sid), token)
    return

################################

def resume(url, sid, token):
    # Resume the scan specified by the sid.
    connect('POST', url, '/scans/{0}/resume'.format(sid), token)
    return

################################

def stop(url, sid, token):
    connect('POST', url, '/scans/{0}/stop'.format(sid), token)
    return

################################

def logout(url, token):
    print('Logging Out...')
    connect('DELETE', url, '/session', token)
    print('Logged Out')
    exit()

################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Control Nessus', formatter_class=RawTextHelpFormatter)

    parser.add_argument("-n", "--nessus", dest='nessus', action="store", metavar='nessus url', type=str, 
		default=None, required=True, help='Nessus url')

    parser.add_argument("-u", "--user", dest='user', action="store", metavar='username', type=str, 
		  default=None, required=True, help='Nessus username')

    parser.add_argument("-P", "--pass", dest='password', action="store_true", default=True, 
      help='Nessus password prompt')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', dest='scan_list', action='store_true', help='List current scans and IDs')
    group.add_argument('-p', '--policies', dest='policy_list', action='store_true', help='List current policies')
    #group.add_argument('-H', '--history', dest='scan_id', type=str, help='List scan history')
    group.add_argument('-sS', '--start', dest='start_scan_id', type=str, help='Start a specified scan using scan id')
    group.add_argument('-pS', '--pause', dest='pause_scan_id', type=str, help='Pause a specified scan using scan id')
    group.add_argument('-sP', '--stop', dest='stop_scan_id', type=str, help='Stop a specified scan using scan id')

    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        print
        exit()

    password = ''
    if args.password:
      password = getpass()

    verify = False
    token = ''

    print('Logging in...')
    try:token = login(args.nessus, args.user, password)
    except: print('Unable to login :('); exit()
    print('Logged in!\n\n')

    #testing
    #get_history_ids(args.nessus, args.scan_id, token)

###### Display all policies  #######
    if args.policy_list:
        print "Printing Policies \n\n"
        policy_dict = get_policies(args.nessus, token)
        print 'Policy Name                              UUID'
        print '--------------------------------------------------'
        for title,uuid in policy_dict.items():
            create_menu(title,uuid, 'Null')


###### Display all scans  #######
    elif args.scan_list:
        temp_status_dict, temp_id_dict = get_scans(args.nessus, token)
        print 'Scan Name                  Status              ID'
        print '-------------------------------------------------'

        for status_name,status in temp_status_dict.items():
            for id_name, id in temp_id_dict.items():
                if status_name == id_name:
                    create_menu(status_name,status, id)


###### Start the scan  #######
    if args.start_scan_id:
        # If -sS [scan_id] flag is passed, start the specified scan
        start_id = args.start_scan_id
        temp_status_dict, temp_id_dict = get_scans(args.nessus, token)

		# Grab the status of the scan and either resume or start based on status
        for key, value in temp_id_dict.items():
            if str(value) == str(start_id):
                if temp_status_dict[key].lower() in ['completed', 'stopped', 'aborted', 'canceled', 'on demand', 'empty']:
                    print('Launching Scan %s') %key
                    launch(args.nessus, start_id, token)

                elif temp_status_dict[key].lower() in ['paused']:
                    print('Resuming Scan %s') %key
                    resume(args.nessus, start_id, token)
                elif temp_status_dict[key].lower() in ['running']:
                    print('Scan already running!')
                    logout(args.nessus, token)
                else:
                    print('Scan completed or unable to start.')
                    print('If you need to start a previously completed scan, add "completed" to the list on line 269')
                    logout(args.nessus, token)

        # Re-grab the scans to get the updated status
        get_status(start_id, args.nessus, token)


###### Pause the scan  #######
    elif args.pause_scan_id:
        pause_id = args.pause_scan_id
        temp_status_dict, temp_id_dict = get_scans(args.nessus, token)
        for key, value in temp_id_dict.items():
            if str(value) == str(pause_id):
                if temp_status_dict[key].lower() in ['paused']:
                    print('Scan already paused!')
                    logout(args.nessus, token)
                elif temp_status_dict[key].lower() in ['running']:
                    print('Pausing Scan %s') %key
                    pause(args.nessus, pause_id, token)
                else:
                    print('Scan unable to be paused')
                    logout(args.nessus, token)

        get_status(pause_id, args.nessus, token)

    elif args.stop_scan_id:
        stop_id = args.stop_scan_id
        temp_status_dict, temp_id_dict = get_scans(args.nessus, token)
        for key, value in temp_id_dict.items():
            if str(value) == str(stop_id):
                if temp_status_dict[key].lower() in ['paused', 'running']:
                    print('Stopping Scan %s') %key
                    stop(args.nessus, stop_id, token)
                    logout(args.nessus, token)
                else:
                    print('Scan cannot be stopped!')
                    logout(args.nessus, token)

        # Re-grab the scans to get the updated status
        get_status(stop_id, args.nessus, token)


