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


# -i device: your network device
# -r range	scan a given range instead of auto scan.
# -s time	time to sleep between each arp request (milliseconds)
# -N		Do not print header.
# -P		print results in a format suitable for parsing by another program

if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 2 ]; then
  LOGNAME="netdiscover_local_live_hosts_$1.txt"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g')
  netdiscover -i $1 -r $2 -s 100 -N -P > $LOGNAME
else
  echo "Please provide your network device and the target ip range."
fi


