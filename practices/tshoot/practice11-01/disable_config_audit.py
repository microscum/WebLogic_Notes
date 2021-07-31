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

# Connect to administration server
connect(username, password, url)

# start an edit session
edit()
# lock the configuration
startEdit()

# go to the root
cd('/')

# set config auditing to None
cmo.setConfigurationAuditType('none')

# Activate changes
save()
activate(block='true')
print '>>>Configuration auditing disabled.'
exit()

