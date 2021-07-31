# Deploys the application (undeploys the old version first)
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 3, 2013
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
target = 'cluster1'
appname = 'contacts'
appsource = '/u01/domains/tshoot/wlsadmin/apps/contacts.war'

# Connect to administration server
connect(username, password, url)

# the deploy command locks the config (and later activates) itself, 
# so do not start an edit session

# if the app is already there, we will undeploy it first
print '>>>Undeploying the old version of the application first.'
try:
   undeployprogress = undeploy(appName=appname)
   '>>>Application undeployed. Continuing...'
except WLSTException:
    print '>>>Application was not there (which is OK). Continuing...'

# deploy new version of app (no deployment plan)
print '>>>Deploying application ' + appname + '. Please wait.'
progress = deploy(appName=appname, path=appsource, targets=target)

# wait for deployment to finish
while progress.isRunning():
   pass

print '>>>Application ' + appname + ' deployed.'

# exit WLST
exit()
