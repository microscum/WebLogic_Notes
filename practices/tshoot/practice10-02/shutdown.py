# Shuts down the managed servers called server3 and server4
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 12, 2013
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
s3 = 'server3'
s4 = 'server4'

# Connect to administration server
connect(username, password, url)

# force shutdown server3 (if already shut down, catch exception)
print '>>>Shutting down ' + s3 + '. Please wait.'
try:
    shutdown(name=s3, entityType='Server', force='true')
except WLSTException:
	pass

# force shutdown server4 (if already shut down, catch exception)
print '>>>Shutting down ' + s4 + '. Please wait.'
try:
    shutdown(name=s4, entityType='Server', force='true')
except WLSTException:
	pass

# exit WLST
exit()
