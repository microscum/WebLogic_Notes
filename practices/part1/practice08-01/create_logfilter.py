# Creates the same log filter and applies it as if you followed the instructions for 
# the practice "Working with WebLogic Server Logs"
#
# Note that this script does not change the server settings "Rotate log file on startup" 
# nor the "Log File Buffer" size, as these would require a server restart and it
# was not desired to stop and start the server as part of this solution script.
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: May 22, 2013
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
filtername = 'clusterfilter'
servname = 'server2'

# Connect to administration server
connect(username, password, url)

# Check if the log filter already exists
try:
	cd('/LogFilters/' + filtername)
	print '>>>The log filter ' + filtername + ' already exists.'
	exit()
except WLSTException:
	pass

print '>>>Creating a new log filter named ' + filtername + '.'

# start an edit session
edit()
# lock the configuration
startEdit()

# go to the root
cd('/')

# Create log filter
filter=create(filtername, 'LogFilter')

# Set the properties
filter.setFilterExpression("(SUBSYSTEM = 'Cluster')")

save()

# Apply the filter to the server log of the 'servname' server
# NOTE: Since the practice has you remove the filter, 
# this code is now commented out.
# cd('/Servers/' + servname + '/Log/' + servname)
# cmo.setLogFileFilter(filter)


# Activate changes
save()
activate(block='true')
print '>>>Log filter created successfully!'
exit()

