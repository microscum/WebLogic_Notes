# Creates a WLDF module
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Sep 30, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# Set variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
moduleName = 'server1-diagnostics'
targetName = 'server1'
samplePeriod = 10000
enabled = false
targetType = 'weblogic.management.runtime.JDBCConnectionPoolRuntimeMBean'
targetAttributes = array(['ActiveConnectionsCurrentCount','CurrCapacity','LeakedConnectionCount'],String)
notifyName = 'jms-notification'
notifyDest = 'wldfnotificationqueue'
notifyFactory = 'weblogic.jms.XAConnectionFactory'
watchName = 'jdbcwatch'
watchExpression = '(${ServerRuntime//[weblogic.management.runtime.JDBCConnectionPoolRuntimeMBean]//ActiveConnectionsCurrentCount} > 0)'
watchAlarm = 'ManualReset'

# Connect to administration server
connect(username, password, url)
 
# Check if WLDF Module already exists
try:
	cd('/WLDFSystemResources/' + moduleName)
	print '>>The WLDF Module ' + moduleName + ' already exists.'
	exit()
except WLSTException:
	pass
 
# Check if harvester already exists
try:
	cd('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/Harvester/' + moduleName + '/HarvestedTypes/' + targetType)
	print 'Collector for MBean type ' + targetType + ' already exists.'
	exit()
except WLSTException:
	pass
 
# Check if notification already exists
try:
	cd('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/WatchNotification/' + moduleName + '/JMSNotifications/' + notifyName)
	print 'Notification ' + notifyName + ' already exists.'
	exit()
except WLSTException:
	pass
 
# Check if watch already exists
try:
	cd('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/WatchNotification/' + moduleName + '/Watches/' + watchName)
	print 'Watch ' + watchName + ' already exists.'
	exit()
except WLSTException:
	pass
 

print '>>>Creating a new WLDF module named ' + moduleName + '.'

edit()
startEdit()
cd('/')


# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create module
module = cmo.createWLDFSystemResource(moduleName)
module.addTarget(targetServer)

# Add collectors to WLDF module
print 'Updating WLDF Module named ' + moduleName + '.'
harvester = getMBean('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/Harvester/' + moduleName)
harvester.setSamplePeriod(samplePeriod)
harvester.setEnabled(enabled)

print 'Adding a new Collector for MBean ' + targetType + '.'
harvestType1 = harvester.createHarvestedType(targetType)
harvestType1.setEnabled(true)
harvestType1.setHarvestedAttributes(targetAttributes)

# Add notification to WLDF module
print 'Updating WLDF Module named ' + moduleName + '.'
print 'Adding a new Notification named ' + notifyName + '.'
notifications = getMBean('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/WatchNotification/' + moduleName)
notifications.setEnabled(enabled)
notify = notifications.createJMSNotification(notifyName)
notify.setEnabled(true)
notify.setDestinationJNDIName(notifyDest)
notify.setConnectionFactoryJNDIName(notifyFactory)

# Add watch to WLDF module
print 'Updating WLDF Module named ' + moduleName + '.'
watches = getMBean('/WLDFSystemResources/' + moduleName + '/WLDFResource/' + moduleName + '/WatchNotification/' + moduleName)
watches.setEnabled(enabled)

print 'Adding a new Watch named ' + watchName + '.'
watch1 = watches.createWatch(watchName)
watch1.setRuleType('Harvester')
watch1.setEnabled(true)
watch1.setRuleExpression(watchExpression)
watch1.setAlarmType(watchAlarm)
watch1.setNotifications(array([notify],weblogic.diagnostics.descriptor.WLDFNotificationBean))


# Activate changes
save()
activate(block='true')
print '>>>WLDF module created successfully.'
exit()

