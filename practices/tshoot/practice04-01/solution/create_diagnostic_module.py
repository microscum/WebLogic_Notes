# Creates a WLDF diagnostic module
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

# Connect to administration server
connect(username, password, url)

# Check if the module already exists
try:
	cd('/WLDFSystemResources/' + moduleName)
	print 'The WLDF Module ' + moduleName + ' already exists.'
	exit()
except WLSTException:
	pass

print 'Creating new WLDF Module named ' + moduleName + '.'

edit()
startEdit()
cd('/')

# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create module
module = cmo.createWLDFSystemResource(moduleName)
module.addTarget(targetServer)

# Activate changes
save()
activate(block='true')
print 'WLDF system diagnostic module created successfully.'
exit()
