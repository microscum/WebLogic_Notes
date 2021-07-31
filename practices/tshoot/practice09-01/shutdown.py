# Shuts down the managed server called server2
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 5, 2013
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
servername = 'server2'

# Connect to administration server
connect(username, password, url)

# force shutdown server2 (if already shut down, catch exception)
print '>>>Shutting down ' + servername + '. Please wait.'
try:
    shutdown(name=servername, entityType='Server', force='true')
except WLSTException:
	pass

# exit WLST
exit()
