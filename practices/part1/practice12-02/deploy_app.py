# Deploys the application to the dynamic cluster
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
target = 'cluster2'
appname = 'supplies'
appsource = '/u01/domains/part1/wlsadmin/apps/supplies.war'

# Connect to administration server
connect(username, password, url)

# the deploy command locks the config (and later activates) itself, 
# so do not start an edit session

# deploy app
print '>>>Deploying application ' + appname + '. Please wait.'
progress = deploy(appName=appname, path=appsource, targets=target)

# wait for deployment to finish
while progress.isRunning():
   pass

print '>>>Application ' + appname + ' deployed.'

# exit WLST
exit()
