# Starts the new managed servers (server3 and server4)
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 7, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
servernamea = 'server3'
servernameb = 'server4'

# Connect to administration server
connect(username, password, url)

# starting a server
print '>>>Starting ' + servernamea + '. Please wait.'
start(name=servernamea, type='Server')

print '>>>Starting ' + servernameb + '. Please wait.'
start(name=servernameb, type='Server')

# exit WLST
exit()
