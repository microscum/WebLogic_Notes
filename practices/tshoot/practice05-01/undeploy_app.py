# Undeploys the application
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: November 27, 2013
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
appname = 'benefits'

# Connect to administration server
connect(username, password, url)

# the undeploy command locks the config (and later activates) itself, 
# so do not start an edit session

# deploy app
print '>>>Undeploying application ' + appname + '. Please wait.'
progress = undeploy(appName=appname)

# wait for deployment to finish
while progress.isRunning():
   pass

print '>>>Application ' + appname + ' undeployed.'

# exit WLST
exit()
