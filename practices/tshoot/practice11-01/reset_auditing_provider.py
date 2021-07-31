# Disables configuration auditing
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 15, 2013
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
domainname = 'wlsadmin'
realmname = 'myrealm'
auditorname = 'change_auditor'

# Connect to administration server
connect(username, password, url)

# start an edit session
edit()
# lock the configuration
startEdit()

try:
	cd('/SecurityConfiguration/' + domainname + '/Realms/' + realmname + '/Auditors/' + auditorname)
	cmo.setSeverity('ERROR')
	# Activate changes
	save()
	activate(block='true')
	print '>>>Auditor level set to ERRROR.'
	exit()

except WLSTException:
	print 'The Auditing Provider ' + auditorname + ' does not exist.'
	exit()

