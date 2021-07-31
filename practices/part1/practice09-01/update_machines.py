# Updates the machines as if you followed the instructions for 
# the practice "Configuring and Using Node Manager"
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
mach1 = 'machine1'
mach2 = 'machine2'

# Connect to administration server
connect(username, password, url)

# start an edit session
edit()
# lock the configuration
startEdit()

# go to the root
cd('/')

# go to first machine and set the node mgr type
cd('Machines')
cd(mach1)
cd('NodeManager')
cd(mach1)
set('NMType', 'Plain')

# go to second machine and set the node mgr type
cd('/Machines/' + mach2 + '/NodeManager/' + mach2)
set('NMType', 'Plain')


save()

# Activate changes
save()
activate(block='true')
print '>>>Configuration of both machines updated successfully!'
exit()

