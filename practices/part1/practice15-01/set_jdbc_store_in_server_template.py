# Updated the server template with a JDBC TLog 
# as if you followed the instructions in
# the practice "Configuring Transaction Persistence"
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: May 23, 2013
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
dsname = 'tlogdatasource1'
jndiname = 'tlogds1'
clustername = 'cluster2'
templatename = 'cluster2server-Template'

# Connect to administration server
connect(username, password, url)

# Check to see if the server template is there
try:
	cd('/ServerTemplates/' + templatename)
except WLSTException:
    print '>>>The Server Template ' + templatename + ' does NOT exist. Exiting.'
    exit()

print '>>>Updating the server template to use the data source named ' + dsname + ' for transaction log.'

# start an edit session
edit()
# lock the configuration
startEdit()

# get the datasource for later
cd('/JDBCSystemResources/' + dsname)
datasource = cmo

# get the cluster as a target for later
cd('/Clusters/' + clustername)
clustertarget = cmo

# go change the template
cd('/ServerTemplates/' + templatename)
cd('TransactionLogJDBCStore/' + templatename)
cmo.setName(templatename)
cmo.setEnabled(true)
cmo.setDataSource(datasource)
cmo.addTarget(clustertarget)


# Activate changes
save()
activate(block='true')
print '>>>Server Template updated successfully!'
exit()

