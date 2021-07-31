# Starts the managed servers (server1 and server2) by starting their cluster (cluster1)
#
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
clustername = 'cluster1'

# Connect to administration server
connect(username, password, url)

# starting both servers in the cluster
print '>>>Starting ' + clustername + '. Please wait.'
start(name=clustername, type='Cluster')

# exit WLST
exit()
