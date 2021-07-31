# Disables the debug flags that were set
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
s1 = 'server1'
s2 = 'server2'
s3 = 'server3'
s4 = 'server4'

# Connect to administration server
connect(username, password, url)

# start an edit session
edit()
# lock the configuration
startEdit()

# go to each of the servers and disable the flags
cd('/Servers/' + s1 + '/ServerDebug/' + s1)
cmo.setDebugReplication(false)
cmo.setDebugHttpSessions(false)
cd('/Servers/' + s2 + '/ServerDebug/' + s2)
cmo.setDebugReplication(false)
cmo.setDebugHttpSessions(false)
cd('/Servers/' + s3 + '/ServerDebug/' + s3)
cmo.setDebugReplication(false)
cmo.setDebugHttpSessions(false)
cd('/Servers/' + s4 + '/ServerDebug/' + s4)
cmo.setDebugReplication(false)
cmo.setDebugHttpSessions(false)

# Activate changes
save()
activate(block='true')

print '>>>Disabled debug flags.'
exit()

