#!/usr/bin/python

# Leonardo Souza - 24/04/2020
# Python External Monitor Template Debug
# Version 1.1.0

# This is a template for external monitor using Python.
# The script is only doing a ping to provide a full example.
# Modify the ping to any other command you need to use.
# Don't forget that anything you output will mark the poll member up.

# From version 11.3.0 at least, the system sets the environment variables
# MON_TMPL_NAME ARGS_I PATH NODE_PORT PWD SHLVL NODE_IP NODE_NAME RUN_I _

# Imports
import sys, os

# All external monitor scripts are called with at least the following arguments.
# When creating the monitor you pass more arguments using arguments section of the monitor.
# You can also create variables that will be available to the script.
# argv[1] = Pool member IP in IPv6 format, need to remove :ffff:
# argv[2] = Pool member port
ip = sys.argv[1][7:]
port = sys.argv[2]

# Log information
pid = str(os.getpid())
os.system("logger -p local0.notice " + os.environ['MON_TMPL_NAME'] + " - PID: " + pid + " Name: " + os.environ['NODE_NAME']  + " IP: " + ip + " Port: " + port)

# Run the command
# -c1 = single ICMP packet
result = os.system("ping -c1 " + ip + "&> /dev/null")
os.system("logger -p local0.notice " + os.environ['MON_TMPL_NAME']  + " - PID: " + pid + " Result: " + str(result))

# Check command result
if result == 0:
    print ("up")