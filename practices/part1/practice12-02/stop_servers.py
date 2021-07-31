# Stops all the servers in the other clusters
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: July 3, 2013
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
target1 = 'cluster1'
target2 = 'cluster3'

# Connect to administration server
connect(username, password, url)

print '>>>Stopping the cluster ' + target1
shutdown(target1,'Cluster',ignoreSessions='true',force='true')

print '>>>Stopping the cluster ' + target2
shutdown(target2,'Cluster',ignoreSessions='true',force='true')
