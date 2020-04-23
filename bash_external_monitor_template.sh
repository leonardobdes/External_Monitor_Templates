#!/bin/bash

# Leonardo Souza - 23/04/2020
# Bash External Monitor Template
# Version 1.0.0

# This is a template for external monitor using Bash.
# The script is only doing a ping to provide a full example.
# Modify the ping to any other command you need to use.
# Don't forget that anything you output will mark the poll member up.

# All external monitor scripts are called with at least the following arguments.
# When creating the monitor you pass more arguments using arguments section of the monitor.
# You can also create variables that will be available to the script.
# $1 = Pool member IP in IPv6 format, need to remove ::ffff:
# $2 = Pool member port
ip=${1:7}
port=$2

# Run the command
# -c1 = single ICMP packet
ping -c1 $ip &> /dev/null
result=$?

# Check command result
[ $result -eq 0 ] && echo "up"