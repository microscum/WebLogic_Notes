# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
targetName = 'server1'

jmsServerName = 'JMSServer1'
maxMessages = 10

jmsModuleName = 'JMSModule1'

factoryName = 'Factory1'
factoryJNDI = 'jms.example.Factory1'

queueName1 = 'Queue1'
queueJNDI1 = 'jms.example.Queue1'
queueName2 = 'Queue2'
queueJNDI2 = 'jms.example.Queue2'
queueName3 = 'Queue3'
queueJNDI3 = 'jms.example.Queue3'
queueTTL = 6000
errqueueName = 'ErrorQueue1'
errqueueJNDI = 'jms.example.ErrorQueue1'

# Connect to administration server
connect(username, password, url)

# Check if JMS Module already exists
try:
	cd('/JMSSystemResources/' + jmsModuleName)
	print 'The JMS Module ' + jmsModuleName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass

# Check if JMS Server already exists
try:
	cd('/JMSServers/' + jmsServerName)
	print 'The JMS Server ' + jmsServerName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass

edit()
startEdit()

# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create JMS Server
print 'Creating new JMS Server named ' + jmsServerName + '.'
jmsServer = create(jmsServerName, 'JMSServer')
jmsServer.setMessagesMaximum(maxMessages)
jmsServer.addTarget(targetServer)

# Create JMS Module
print 'Creating new JMS Module named ' + jmsModuleName + '.'
jmsSystemResource = create(jmsModuleName, 'JMSSystemResource')
jmsSystemResource.addTarget(targetServer)
jmsResource = getMBean('/JMSSystemResources/' + jmsModuleName + '/JMSResource/' + jmsModuleName)

# Create JMS Connection Factory
print 'Creating new Connection Factory named ' + factoryName + '.'
factory = jmsResource.createConnectionFactory(factoryName)
factory.setDefaultTargetingEnabled(true)
factory.setJNDIName(factoryJNDI)
deliveryParams = factory.getDefaultDeliveryParams()
xaParams = factory.getTransactionParams()
xaParams.setXAConnectionFactoryEnabled(true)

# Create JMS Sub-deployment
print 'Creating new Subdeployment in the JMS Module for ' + jmsServerName + '.'
subDeploymentName = 'DeployTo' + jmsServerName
jmsSubDeployment = jmsSystemResource.createSubDeployment(subDeploymentName)
jmsSubDeployment.addTarget(jmsServer)

# Create JMS error destination
print 'Creating new Queue named ' + errqueueName + '.'
queue = jmsResource.createQueue(errqueueName)
queue.setJNDIName(errqueueJNDI)
queue.setSubDeploymentName(subDeploymentName)

# Create JMS destinations
print 'Creating new Queue named ' + queueName1 + '.'
queue = jmsResource.createQueue(queueName1)
queue.setJNDIName(queueJNDI1)
queue.setSubDeploymentName(subDeploymentName)

print 'Creating new Queue named ' + queueName2 + '.'
queue = jmsResource.createQueue(queueName2)
queue.setJNDIName(queueJNDI2)
queue.setSubDeploymentName(subDeploymentName)
deliveryOverrides = queue.getDeliveryParamsOverrides()
deliveryOverrides.setTimeToLive(queueTTL)

print 'Creating new Queue named ' + queueName3 + '.'
queue = jmsResource.createQueue(queueName3)
queue.setJNDIName(queueJNDI3)
queue.setSubDeploymentName(subDeploymentName)


# Activate changes
save()
activate(block='true')
print 'JMS Server and Module created successfully.'

exit()
