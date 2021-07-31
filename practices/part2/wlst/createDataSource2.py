
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

# Modify these values as necessary
url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
dsName = 'AuctionDBDataSource2'
dsJNDIName = 'jdbc.AuctionDB2'
targetName = 'cluster1'
initialCapacity = 5
maxCapacity = 10
capacityIncrement = 1
driverName = 'oracle.jdbc.xa.client.OracleXADataSource'
driverURL = 'jdbc:oracle:thin:@host02.example.com:7521:orcl2'
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
targetServer = getMBean('/Clusters/' + targetName)

# Create data source
jdbcSystemResource = create(dsName, 'JDBCSystemResource')
jdbcResource = jdbcSystemResource.getJDBCResource()
jdbcResource.setName(dsName)

# Set JNDI name
jdbcResourceParameters = jdbcResource.getJDBCDataSourceParams()
jdbcResourceParameters.setJNDINames([dsJNDIName])
jdbcResourceParameters.setGlobalTransactionsProtocol('TwoPhaseCommit')

# Create connection pool
connectionPool = jdbcResource.getJDBCConnectionPoolParams()
connectionPool.setInitialCapacity(initialCapacity)
connectionPool.setMaxCapacity(maxCapacity)
connectionPool.setCapacityIncrement(capacityIncrement)

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

