#!/usr/bin/python

# Leonardo Souza - 23/04/2020
# Python External Monitor Template Debug
# Version 1.0.0

# This is a template for external monitor using Python.
# The script is only doing a ping to provide a full example.
# Modify the ping to any other command you need to use.
# Don't forget that anything you output will mark the poll member up.

# Imports
import sys, os

# All external monitor scripts are called with at least the following arguments.
# When creating the monitor you pass more arguments using arguments section of the monitor.
# You can also create variables that will be available to the script.
# argv[1] = Pool member IP in IPv6 format, need to remove :ffff:
# argv[2] = Pool member port
ip = sys.argv[1][7:]
port = sys.argv[2]

# Run the command
# -c1 = single ICMP packet
result = os.system("ping -c1 " + ip + "&> /dev/null")

# Check command result
if result == 0:
    print ("up")