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
jmsModuleName = 'JMSModule1'

templateName = 'Template1'

factoryName = 'Factory1'
factoryJNDI = 'jms.example.Factory1'
factoryTTL = 360000
factoryTimeout = 600000

queueName = 'Queue1'
queueJNDI = 'jms.example.Queue1'
topicName = 'Topic1'
topicJNDI = 'jms.example.Topic1'
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
deliveryParams.setDefaultTimeToLive(factoryTTL)
deliveryParams.setSendTimeout(factoryTimeout)
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

# Create JMS template
print 'Creating new Template named ' + templateName + '.'
template = jmsResource.createTemplate(templateName)
failureParams = template.getDeliveryFailureParams()
failureParams.setExpirationPolicy('Redirect')
failureParams.setErrorDestination(queue)

# Create JMS destinations
print 'Creating new Queue named ' + queueName + ' with template ' + templateName + '.'
queue = jmsResource.createQueue(queueName)
queue.setJNDIName(queueJNDI)
queue.setSubDeploymentName(subDeploymentName)
queue.setTemplate(template)

print 'Creating new Topic named ' + topicName + ' with template ' + templateName + '.'
topic = jmsResource.createTopic(topicName)
topic.setJNDIName(topicJNDI)
topic.setSubDeploymentName(subDeploymentName)
topic.setTemplate(template)

# Activate changes
save()
activate(block='true')
print 'JMS Server and Module created successfully.'

exit()
