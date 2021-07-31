
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
wmNames = ['MinThreadsWM','MaxThreadsWM']
constNames = ['MinThreads10','MaxThreads5']
constThreads = [10,5]
targetName = 'cluster1'

# Connect to administration server
connect(username, password, url)

# Check if first work manager already exists
try:
    for wmName in wmNames:
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + wmName)
        print 'The Work Manager ' + wmName + ' already exists.'
	exit()
except WLSTException:
	pass

edit()
startEdit()
cd('/')

# Save reference to target
targetServer = getMBean('/Clusters/' + targetName)

tuning = getMBean('/SelfTuning/' + domainName)

# Create work managers
i=0
for wmName in wmNames:
    print 'Creating new Work Manager named ' + wmName + '.'    
    wm = tuning.createWorkManager(wmName)
    wm.addTarget(targetServer)

    # Add constraint to work manager
    print 'Adding new constraint named ' + constNames[i] + '.'

    if i == 0:
        constraint = tuning.createMinThreadsConstraint(constNames[i])
        constraint.setCount(constThreads[i])
        constraint.addTarget(targetServer)
        wm.setMinThreadsConstraint(constraint)
    else:
        constraint = tuning.createMaxThreadsConstraint(constNames[i])
        constraint.setCount(constThreads[i])
        constraint.addTarget(targetServer)
        constraint.unSet('ConnectionPoolName')
        wm.setMaxThreadsConstraint(constraint)
        wm.setIgnoreStuckThreads(false)

    i += 1

# Activate changes
save()
activate(block='true')
print 'Work Manager configuration complete.'
exit()



