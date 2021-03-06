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

RED='\033[0;31m'
NC='\033[0m' # No Color
dd=$(date +"%Y-%m-%d-%H-%M")
logfile='icmp-live-hosts.txt'

if [ $# -eq 1 ]; then
	file=$1
	echo "---- $dd ----" >> $logfile
	while IFS= read -r ipaddr
	do
		echo "Pinging $ipaddr.."
		response=$(ping -c 1 -W 1 $ipaddr | grep 'bytes from' | cut -d' ' -f4 |sed 's/://')
		if [ ! -z "$response" ]; then
			printf "${RED}%s${NC} responds..\n" "$ipaddr"
			echo "$ipaddr" >> $logfile
		fi
	done <"$file"
else
	echo "Please provide a file containing a list of IP addresses."
fi
