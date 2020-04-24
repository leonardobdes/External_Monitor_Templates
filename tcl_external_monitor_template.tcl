#!/usr/bin/tclsh

# Leonardo Souza - 24/04/2020
# Tcl External Monitor Template Debug
# Version 1.1.0

# This is a template for external monitor using Bash.
# The script is only doing a ping to provide a full example.
# Modify the ping to any other command you need to use.
# Don't forget that anything you output will mark the poll member up.

# All external monitor scripts are called with at least the following arguments.
# When creating the monitor you pass more arguments using arguments section of the monitor.
# You can also create variables that will be available to the script.
# $argv 0 = Pool member IP in IPv6 format, need to remove ::ffff:
# $argv 1 = Pool member port
set ip [string range [lindex  $argv 0] 7 end]
set port [lindex  $argv 1]

# Run the command
# -c1 = single ICMP packet
set result [catch {exec ping -c1 $ip}]

# Check command result
if {$result == 0} {puts "up"}