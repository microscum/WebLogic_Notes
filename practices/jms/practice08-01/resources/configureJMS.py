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

serverName1 = 'server1'
serverName2 = 'server2'
serverName3 = 'server3'
clusterName = 'cluster1'

dsName = 'OracleDS1-NoXA'
dsJNDIName = 'jdbc.example.' + dsName
initialCapacity = 2
maxCapacity = 10
capacityIncrement = 1
driverName = 'oracle.jdbc.driver.OracleDriver'
driverURL = 'jdbc:oracle:thin:@host02.example.com:1521:orcl'
driverUsername = 'oracle'
driverPassword = 'Welcome1'

storeName1 = 'JDBCStore1'
storeName2 = 'JDBCStore2'
storeName3 = 'JDBCStore3'

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


edit()
startEdit()

# Save reference to target cluster
targetCluster = getMBean('/Clusters/' + clusterName)

# Create Data Source
print 'Creating new Data Source named ' + dsName + '.'
jdbcSystemResource = create(dsName, 'JDBCSystemResource')
jdbcResource = jdbcSystemResource.getJDBCResource()
jdbcResource.setName(dsName)
jdbcResourceParameters = jdbcResource.getJDBCDataSourceParams()
jdbcResourceParameters.setJNDINames([dsJNDIName])
jdbcResourceParameters.setGlobalTransactionsProtocol('None')
connectionPool = jdbcResource.getJDBCConnectionPoolParams()
connectionPool.setInitialCapacity(initialCapacity)
connectionPool.setMaxCapacity(maxCapacity)
connectionPool.setCapacityIncrement(capacityIncrement)
connectionPool.setTestConnectionsOnReserve(true)
driver = jdbcResource.getJDBCDriverParams()
driver.setDriverName(driverName)
driver.setUrl(driverURL)
driver.setPassword(driverPassword)
driverProperties = driver.getProperties()
userProperty = driverProperties.createProperty('user')
userProperty.setValue(driverUsername)
jdbcSystemResource.addTarget(targetCluster)

# Create first Store
print 'Creating new Persistent Store named ' + storeName1 + '.'
jdbcStore1 = create(storeName1, 'JDBCStore')
jdbcStore1.setDataSource(jdbcSystemResource)
jdbcStore1.setPrefixName(storeName1)

# Create second Store
print 'Creating new Persistent Store named ' + storeName2 + '.'
jdbcStore2 = create(storeName2, 'JDBCStore')
jdbcStore2.setDataSource(jdbcSystemResource)
jdbcStore2.setPrefixName(storeName2)

# Create third Store
print 'Creating new Persistent Store named ' + storeName3 + '.'
jdbcStore3 = create(storeName3, 'JDBCStore')
jdbcStore3.setDataSource(jdbcSystemResource)
jdbcStore3.setPrefixName(storeName3)

# Create first JMS Server
print 'Creating new JMS Server named ' + jmsServerName1 + '.'
jmsServer1 = create(jmsServerName1, 'JMSServer')
jmsServer1.setPersistentStore(jdbcStore1)

# Create second JMS Server
print 'Creating new JMS Server named ' + jmsServerName2 + '.'
jmsServer2 = create(jmsServerName2, 'JMSServer')
jmsServer2.setPersistentStore(jdbcStore2)

# Create third JMS Server
print 'Creating new JMS Server named ' + jmsServerName3 + '.'
jmsServer3 = create(jmsServerName3, 'JMSServer')
jmsServer3.setPersistentStore(jdbcStore3)

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
