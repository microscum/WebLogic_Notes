# Redeploys the application
#
# By: ST Curriculum Development Team
# Version 1.1
# Last updated: Dec 20, 2013
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
appname = 'contacts'
appsource = '/u01/domains/tshoot/wlsadmin/apps/contacts.war'
target = 'cluster1'

# Connect to administration server
connect(username, password, url)

# the deploy and redeploy commands lock the config (and later activate), 
# so do not start an edit session

# Get a reference to the contacts app
deploymentref = getMBean('AppDeployments/' + appname)
# check to see if contacts has been deployed before (the ref is not None)
if (deploymentref != None):
	# contacts there, doing a redeploy
	print '>>>Redeploying application ' + appname + '. Please wait.'
	progress = redeploy(appName=appname)
	# wait for deployment to finish
	while progress.isRunning():
		pass
	print '>>>Application ' + appname + ' redeployed.'
else:
	# contacts not there, doing a deploy
	print '>>>The app was not deployed before, so deploying  ' + appname + ' (rather than redeploying). Please wait.'
	progress = deploy(appName=appname, path=appsource, targets=target)
	# wait for deployment to finish
	while progress.isRunning():
		pass
	print '>>>Application ' + appname + ' deployed.' 

# exit WLST
exit()
