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
targetName = 'dyncluster1'
jmsServerName = 'HR-JMSServer1'
jmsModuleName = 'HR-JMSModule'

factoryName = 'Factory1'
factoryJNDI = 'jms.hr.Factory1'
# 5 minute TTL
factoryTTL = 300000
factoryTimeout = 30000

templateName = 'HRTemplate'
queueName = 'NewEmployeeQueue'
queueJNDI = 'jms.hr.NewEmployeeQueue'
topicName = 'BenefitsTopic'
topicJNDI = 'jms.hr.BenefitsTopic'
errqueueName = 'ErrorQueue'
errqueueJNDI = 'jms.hr.ErrorQueue'

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

# Save reference to target cluster
targetCluster = getMBean('/Clusters/' + targetName)

# Create JMS Server
print 'Creating new JMS Server named ' + jmsServerName + '.'
jmsServer = create(jmsServerName, 'JMSServer')
jmsServer.addTarget(targetCluster)

# Create JMS Module
print 'Creating new JMS Module named ' + jmsModuleName + '.'
jmsSystemResource = create(jmsModuleName, 'JMSSystemResource')
jmsSystemResource.addTarget(targetCluster)
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
subDeploymentName = 'DeployTo-' + jmsServerName
jmsSubDeployment = jmsSystemResource.createSubDeployment(subDeploymentName)
jmsSubDeployment.addTarget(jmsServer)

# Create JMS error destination
print 'Creating new Distributed Queue named ' + errqueueName + '.'
queue = jmsResource.createUniformDistributedQueue(errqueueName)
queue.setJNDIName(errqueueJNDI)
queue.setSubDeploymentName(subDeploymentName)

# Create JMS template
print 'Creating new Template named ' + templateName + '.'
template = jmsResource.createTemplate(templateName)
failureParams = template.getDeliveryFailureParams()
failureParams.setExpirationPolicy('Redirect')
failureParams.setErrorDestination(queue)

# Create JMS destinations
print 'Creating new Distributed Queue named ' + queueName + ' with template ' + templateName + '.'
queue = jmsResource.createUniformDistributedQueue(queueName)
queue.setJNDIName(queueJNDI)
queue.setSubDeploymentName(subDeploymentName)
queue.setTemplate(template)

print 'Creating new Distributed Topic named ' + topicName + ' with template ' + templateName + '.'
topic = jmsResource.createUniformDistributedTopic(topicName)
topic.setJNDIName(topicJNDI)
topic.setForwardingPolicy('Partitioned')
topic.setSubDeploymentName(subDeploymentName)
topic.setTemplate(template)

# Activate changes
save()
activate(block='true')
print 'JMS Server and Module created successfully.'

exit()
