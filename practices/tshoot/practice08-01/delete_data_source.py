# Deletes the old data source (if it exists). This seemed easier than putting the 'check for it'
# code in a 'modify' data source script (especially since the create script already existed)
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 30, 2013
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
dsname = 'datasource1'

# Connect to administration server
connect(username, password, url)

# Check if data source already exists and if it does, delete it
mbeanref = getMBean('/JDBCSystemResources/' + dsname)
if (mbeanref == None):
    print 'The data source ' + dsname + ' does not exist. That is OK. It will be created in the next script.'
    disconnect()	
    exit()
else:
    pass

print '>>>Deleting the old version of the data source ' + dsname + '.'
# start an edit session
edit()
# lock the configuration
startEdit()
cd('/')
cmo.destroyJDBCSystemResource(getMBean('/JDBCSystemResources/' + dsname))
# Activate changes
save()
activate(block='true')
exit()

