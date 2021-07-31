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
dsName = 'OracleDS1-NoXA'
dsJNDIName = 'jdbc.example.' + dsName
targetName = 'server1'
initialCapacity = 2
maxCapacity = 10
capacityIncrement = 1
driverName = 'oracle.jdbc.driver.OracleDriver'
driverURL = 'jdbc:oracle:thin:@host02.example.com:1521:orcl'
driverUsername = 'oracle'
driverPassword = 'Welcome1'

# Connect to administration server
connect(username, password, url)

# Check if data source already exists
try:
	cd('/JDBCSystemResources/' + dsName)
	print 'The JDBC Data Source ' + dsName + ' already exists.'
	exit()
except WLSTException:
	pass

print 'Creating new JDBC Data Source named ' + dsName + '.'

edit()
startEdit()
cd('/')

# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Create data source
jdbcSystemResource = create(dsName, 'JDBCSystemResource')
jdbcResource = jdbcSystemResource.getJDBCResource()
jdbcResource.setName(dsName)

# Set JNDI name and XA
jdbcResourceParameters = jdbcResource.getJDBCDataSourceParams()
jdbcResourceParameters.setJNDINames([dsJNDIName])
jdbcResourceParameters.setGlobalTransactionsProtocol('None')

# Create connection pool
connectionPool = jdbcResource.getJDBCConnectionPoolParams()
connectionPool.setInitialCapacity(initialCapacity)
connectionPool.setMaxCapacity(maxCapacity)
connectionPool.setCapacityIncrement(capacityIncrement)
connectionPool.setTestConnectionsOnReserve(true)

# Create driver settings
driver = jdbcResource.getJDBCDriverParams()
driver.setDriverName(driverName)
driver.setUrl(driverURL)
driver.setPassword(driverPassword)
driverProperties = driver.getProperties()
userProperty = driverProperties.createProperty('user')
userProperty.setValue(driverUsername)

# Set data source target
jdbcSystemResource.addTarget(targetServer)

# Activate changes
save()
activate(block='true')
print 'Data Source created successfully.'
exit()
