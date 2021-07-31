# Creates a JMS Server, JMS module, a subdeployment, and a queue
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
jmsModuleName = 'jmsmodule1'
jmsServerName = 'jmsserver1'
queueName = 'wldfnotificationqueue'
queueJNDIName = 'wldfnotificationqueue'
targetName = 'server1'

# Connect to administration server
connect(username, password, url)

# Check if JMS Module already exists
try:
	cd('/JMSSystemResources/' + jmsModuleName)
	print 'The JMS Module ' + jmsModuleName + ' already exists.'
	exit()
except WLSTException:
	pass

# Check if JMS Server already exists
try:
	cd('/JMSServers/' + jmsServerName)
	print 'The JMS Server ' + jmsServerName + ' already exists.'
	exit()
except WLSTException:
	pass

# Check if Queue already exists
try:
	cd('/JMSSystemResources/' + jmsModuleName + '/JMSResource/' + jmsModuleName + '/Queues/' + queueName)
	print 'The JMS Queue ' + queueName + ' already exists.'
	exit()
except WLSTException:
	pass

edit()
startEdit()
cd('/')

print 'Creating new JMS Server named ' + jmsServerName + '.'
# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create JMS Server and Module
jmsServer = create(jmsServerName, 'JMSServer')
jmsSystemResource = create(jmsModuleName, 'JMSSystemResource')

# Target JMS Server and Module
jmsServer.addTarget(targetServer)
jmsSystemResource.addTarget(targetServer)

# Create JMS Sub-deployment
subDeploymentName = 'DeployTo' + jmsServerName
jmsSubDeployment = jmsSystemResource.createSubDeployment(subDeploymentName)
jmsSubDeployment.addTarget(jmsServer)

# Create and target JMS Queue
jmsResource = getMBean('/JMSSystemResources/' + jmsModuleName + '/JMSResource/' + jmsModuleName)
print 'Creating new Queue named ' + queueName + '.'
queue = jmsResource.createQueue(queueName)
queue.setJNDIName(queueJNDIName)
queue.setSubDeploymentName(subDeploymentName)

# Activate changes
save()
activate(block='true')
print 'JMS Module updated successfully.'
exit()
