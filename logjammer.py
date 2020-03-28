#!/usr/bin/env python3

from collections import deque

# Quick thingy to jam Apache logs together.

# Problem: The error log won't show which request the error output belongs to.
# Solution: Configure the logs to show a "Request ID" (%L in the log format)
#     and run this on them.

# This is free and unencumbered software released into the public domain.
# See UNLICENSE.txt for details.

##############################################################
# Config, these should probably come from command line
access_log = "/var/log/apache2/access.log"
access_log_field = 6
error_log = "/var/log/apache2/error.log"
error_log_field = 4
timeout = 3   # errors outside this time frame might not be bundled


##############################################################
# Storage for error log lines
entries = {}
def store( tag, text ):
    if not tag in entries:
        entries[tag] = deque()
    entries[tag].append( text )

def flush( tag ):
    if tag in entries:
        while len( entries[tag] ) > 0:
            print( "   " + entries[tag].popleft(), end="" )
        del entries[tag]



##############################################################
# Main logic: open files, go into "tail -f" loop on both files
f_a = open(access_log, 'r')
f_e = open(error_log, 'r')
f_a.seek(0,2)
f_e.seek(0,2)

while True:
    l = f_a.readline()
    if l != '':
        # I assume access log entries are written only after request
        # completed and all errors are in?
        # Might not be 100% foolproof for long-running PHP etc.?
        print( l, end="" )
        flush( l.split()[access_log_field-1])
    l = f_e.readline()
    if l != '':
        store( l.split()[error_log_field-1], l )


        
        
