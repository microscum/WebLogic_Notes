# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host02:7001'
username = 'weblogic'
password = 'Welcome1'

targetName = 'cluster1'

jmsServerName1 = 'JMSServer1'
jmsServerName2 = 'JMSServer2'
jmsServerName3 = 'JMSServer3'

jmsModuleName = 'JMSModule1'

factoryName = 'Factory1'
factoryJNDI = 'jms.example.Factory1'
factoryTTL = 1800000
factoryTimeout = 600000

queueName = 'DistQueue1'
queueJNDI = 'jms.example.Queue1'
topicName = 'DistTopic1'
topicJNDI = 'jms.example.Topic1'


# Connect to administration server
connect(username, password, url)

# Check if JMS Module already exists
try:
	cd('/JMSSystemResources/' + jmsModuleName)
	print 'The JMS Module ' + jmsModuleName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass


edit()
startEdit()

# Save reference to target cluster
targetCluster = getMBean('/Clusters/' + targetName)

# Save reference to JMS servers
jmsServer1 = getMBean('/JMSServers/' + jmsServerName1)
jmsServer2 = getMBean('/JMSServers/' + jmsServerName2)
jmsServer3 = getMBean('/JMSServers/' + jmsServerName3)

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
lbParams = factory.getLoadBalancingParams()
lbParams.setServerAffinityEnabled(false)

# Create JMS Sub-deployment
print 'Creating new Subdeployment in the JMS Module for all JMS Servers.'
subDeploymentName = 'DeployTo-AllJMSServers'
jmsSubDeployment = jmsSystemResource.createSubDeployment(subDeploymentName)
jmsSubDeployment.addTarget(jmsServer1)
jmsSubDeployment.addTarget(jmsServer2)
jmsSubDeployment.addTarget(jmsServer3)

# Create JMS destinations
print 'Creating new Distributed Queue named ' + queueName + '.'
queue = jmsResource.createUniformDistributedQueue(queueName)
queue.setJNDIName(queueJNDI)
queue.setSubDeploymentName(subDeploymentName)

print 'Creating new Partitioned Distributed Topic named ' + topicName + '.'
topic = jmsResource.createUniformDistributedTopic(topicName)
topic.setJNDIName(topicJNDI)
topic.setForwardingPolicy('Partitioned')
topic.setSubDeploymentName(subDeploymentName)

# Activate changes
save()
activate(block='true')
print 'All JMS resources created successfully.'

exit()
