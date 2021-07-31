# Target the data source to the dynamic cluster
# as if you followed the directions in dynamic cluster practice
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: April 25, 2013
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
clustername = 'cluster2'
dsname = 'datasource1'

# Connect to administration server
connect(username, password, url)

# start an edit session
edit()
# lock the configuration
startEdit()

# go get the cluster as the target
cd('/Clusters/' + clustername)
target = cmo

# go to the data source
cd('/JDBCSystemResources/' + dsname)
# add the cluster as a target
cmo.addTarget(target)

# Activate changes
save()
activate(block='true')
print '>>>Data source ' + dsname + ' is targeted to ' + clustername + '.'
exit()
