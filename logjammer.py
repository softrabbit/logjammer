#!/usr/bin/python3

# Quick thingy to jam Apache logs together.

# Problem: The error log won't show which request the error output belongs to.
# Solution: Configure the logs to show a "Request ID" (%L in the log format)
#     and run this on them.



# These should probably come from command line
access_log = "/var/log/apache2/access.log"
error_log_field = 6
error_log = "/var/log/apache2/error.log"
error_log_field = 4
timeout = 3   # errors outside this time frame might not be bundled


# Main logic: open files, go into "tail -f" loop on both files
f_a = open(access_log, 'r')
f_e = open(error_log, 'r')
f_a.seek(0,2)
f_e.seek(0,2)

while True:
    l=f_a.readline()
    if l != '':
        print(l, end="")
    l=f_e.readline()
    if l != '':
        print(l, end="")
        
