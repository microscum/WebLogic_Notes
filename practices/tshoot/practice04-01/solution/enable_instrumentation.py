# Enables instrumentation on the server
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 3, 2013
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
moduleName = 'server1-diagnostics'
targetName = 'server1'
enabled = true

# Connect to administration server
connect(username, password, url)

# Check if WLDF module exists
try:
	cd('/WLDFSystemResources/' + moduleName)
except WLSTException:
	print 'The WLDF Module ' + moduleName + ' does not exist.'
	exit()
edit()
startEdit()
cd('/')

# Enable instrumentation at server level (can still be disabled in app-scoped modules)
print 'Updating WLDF diagnostic module named ' + moduleName + '.'
inst = getMBean('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/Instrumentation/' + moduleName)
inst.setEnabled(enabled)

# Activate changes
save()
activate(block='true')
print 'WLDF diagnostic module updated successfully.'
exit()
