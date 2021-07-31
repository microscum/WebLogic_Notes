# Disables the WLDF module by setting its target to no server or cluster
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 23, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# Set variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
moduleName = 'server1-diagnostics'

# Connect to administration server
connect(username, password, url)
 
# Check if the WLDF Module exists
# if it does not exit
try:
	cd('/WLDFSystemResources/' + moduleName)
except WLSTException:
	exit()

# if we get to here, the diagnostic module exists, so work on it
edit()
startEdit()
cd('/WLDFSystemResources/' + moduleName)
set('Targets',jarray.array([], ObjectName))
save()
activate(block='true')
print '>>>The WLDF Module ' + moduleName + ' disabled (targeted to nothing) successfully.'

