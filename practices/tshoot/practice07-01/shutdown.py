# Shuts down the managed servers (server1 and server2)
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 30, 2013
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
server1 = 'server1'
server2 = 'server2'

# Connect to administration server
connect(username, password, url)

# force shutdown server1 (if already shut down, catch exception)
print '>>>Shutting down ' + server1 + '. Please wait.'
try:
    shutdown(name=server1, entityType='Server', force='true')
except WLSTException:
	pass

# force shutdown server2 (if already shut down, catch exception)
print '>>>Shutting down ' + server2 + '. Please wait.'
try:
    shutdown(name=server2, entityType='Server', force='true')
except WLSTException:
	pass

# exit WLST
exit()
