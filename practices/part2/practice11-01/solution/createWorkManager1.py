
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# Modify these values as necessary
url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
wmName = 'HighPriorityWM'
rqName = 'FairShare90'
rqFairShare = 90
targetName = 'server1'

# Connect to administration server
connect(username, password, url)

# Check if first work manager already exists
try:
	cd('/SelfTuning/' + domainName + '/WorkManagers/' + wmName)
	print 'The Work Manager ' + wmName + ' already exists.'
	exit()
except WLSTException:
	pass

edit()
startEdit()
cd('/')

# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create work manager
print 'Creating new Work Manager named ' + wmName + '.'tuning = getMBean('/SelfTuning/' + domainName)
wm = tuning.createWorkManager(wmName)
wm.addTarget(targetServer)

# Add request class to work manager
print 'Adding new Request Class named ' + rqName + '.'rq = tuning.createFairShareRequestClass(rqName)
rq.setFairShare(rqFairShare)
rq.addTarget(targetServer)
wm.setFairShareRequestClass(rq)

# Activate changes
save()
activate(block='true')
print 'Work Manager created successfully.'
exit()

