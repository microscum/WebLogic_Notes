# Redeploys the old contacts app 
# as if you followed the directions in 
# the practice "Configuring Transaction Persistence"
#
# By: ST Curriculum Development Team
# Version 1.1
# Last updated: June 4, 2013
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
appname = 'contacts'
appsource = '/u01/domains/part1/wlsadmin/apps/contacts.war'


# Connect to administration server
connect(username, password, url)

# the undeploy and redeploy commands lock the config (and later activate) themselves, 
# so do not start an edit session

# since it is perhaps targeted wrong, we'll undeploy it first (if there)
print '>>>Undeploying the old version of the application first.'
try:
	undeploymentprogress = undeploy(appName=appname)
	'>>>Application undeployed. Continuing...'
except WLSTException:
	print '>>>Application was not there (which is OK). Continuing...'

# deploy app
print '>>>Deploying application ' + appname + '. Please wait.'
progress = deploy(appName=appname, path=appsource, targets=target)

# wait for deployment to finish
while progress.isRunning():
	pass

print '>>>Application ' + appname + ' deployed.'

# exit WLST
exit()
