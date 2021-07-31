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

dsName = 'OracleDS1-NoXA'
dsJNDIName = 'jdbc.example.' + dsName
initialCapacity = 2
maxCapacity = 10
capacityIncrement = 1
driverName = 'oracle.jdbc.driver.OracleDriver'
driverURL = 'jdbc:oracle:thin:@host02.example.com:1521:orcl'
driverUsername = 'oracle'
driverPassword = 'Welcome1'

storeName = 'JDBCStore1'

jmsServerName = 'JMSServer1'
jmsModuleName = 'JMSModule1'

factoryName = 'Factory1'
factoryJNDI = 'jms.example.Factory1'
factoryTTL = 1800000
factoryTimeout = 600000


# Connect to administration server
connect(username, password, url)

# Check if data source already exists
try:
	cd('/JDBCSystemResources/' + dsName)
	print 'The JDBC Data Source ' + dsName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass

# Check if the store already exists
try:
	cd('/JDBCStores/' + storeName)
	print 'The JDBC Store ' + storeName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass

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

# Create Data Source, do not target
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

# Create Store, do not target
print 'Creating new Persistent Store named ' + storeName + '.'
jdbcStore = create(storeName, 'JDBCStore')
jdbcStore.setDataSource(jdbcSystemResource)

# Create JMS Server, do not target
print 'Creating new JMS Server named ' + jmsServerName + '.'
jmsServer = create(jmsServerName, 'JMSServer')
jmsServer.setPersistentStore(jdbcStore)

# Create JMS Module, do not target
print 'Creating new JMS Module named ' + jmsModuleName + '.'
jmsSystemResource = create(jmsModuleName, 'JMSSystemResource')
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

# Activate changes
save()
activate(block='true')
print 'All JMS resources created successfully.'

exit()
