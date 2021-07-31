# Deletes the two new servers
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

# start an edit session
edit()
# lock the configuration
startEdit()

# go to the root
cd('/')

# Save a reference to each server
s3ref = getMBean('/Servers/' + s3)
s4ref = getMBean('/Servers/' + s4)

# Remove the machine and cluster from each
s3ref.setCluster(None)
s3ref.setMachine(None)
s4ref.setCluster(None)
s4ref.setMachine(None)

# remove any references to these servers
editService.getConfigurationManager().removeReferencesToBean(s3ref)
editService.getConfigurationManager().removeReferencesToBean(s4ref)

# go back to root and destroy server3
cd('/')
cmo.destroyServer(s3ref)

# go back to root and destroy server4
cd('/')
cmo.destroyServer(s4ref)

# Activate changes
save()
activate(block='true')
print '>>>Servers removed successfully!'
exit()

