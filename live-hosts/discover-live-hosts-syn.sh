#!/bin/bash

#    This file is part of PenTestKit
#    Copyright (C) 2017 @maldevel
#    https://github.com/maldevel/PenTestKit
#    
#    PenTestKit - Useful tools for Penetration Testing.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   
#    For more see the file 'LICENSE' for copying permission.


# -n    	Never do DNS resolution
# -sn   	Ping Scan - disable port scan
# -PS[portlist] TCP SYN discovery to given ports
# -oA   	Output in the three major formats at once

if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  LOGNAME="tcp_syn_live_hosts_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g')
  nmap -n -sn -PS21,22,23,25,53,80,88,110,135,139,143,443,445,465,587,993,995,1433,3306,3389,8080,8443 -oA $LOGNAME $1 | grep 'report' | sed 's/Nmap scan report for //'
else
    echo "Please provide the target ip range."
fi


