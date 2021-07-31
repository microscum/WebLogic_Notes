# Creates a data source that works
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Oct 30, 2014
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
dsname = 'datasource1'
jndiname = 'datasource1'
clustername = 'cluster1'
initialcap = 1
maxcap = 5
mincap = 1
cachetype = 'LRU'
cachesize = 15
testreserve = true
testfreq = 240
trustidle = 60
shrink = 300
# inactive connection timeout is 0 so that inactive connections are never reclaimed
inactivetimeout = 0
drivername = 'oracle.jdbc.xa.client.OracleXADataSource'
driverurl = 'jdbc:oracle:thin:@host02.example.com:1521:orcl'
driveruser = 'oracle'
driverpassword = 'Welcome1'
testtable='SQL SELECT 1 FROM DUAL'

# Connect to administration server
connect(username, password, url)

# Check if data source already exists
try:
	cd('/JDBCSystemResources/' + dsname)
	print '>>>The JDBC Data Source ' + dsname + ' already exists.'
	exit()
except WLSTException:
	pass

print '>>>Creating a replacement JDBC data source named ' + dsname + '.'

# start an edit session
edit()
# lock the configuration
startEdit()


# Save a reference to the target cluster
cd('/Clusters')
cd(clustername)
target = cmo

# go back to the root
cd('/')

# Create data source
jdbcresource = create(dsname, 'JDBCSystemResource')
theresource = jdbcresource.getJDBCResource()
theresource.setName(dsname)

# Set JNDI name
jdbcresourceparams = theresource.getJDBCDataSourceParams()
jdbcresourceparams.setJNDINames([jndiname])
jdbcresourceparams.setGlobalTransactionsProtocol('TwoPhaseCommit')

# Create connection pool
pool = theresource.getJDBCConnectionPoolParams()
pool.setInitialCapacity(initialcap)
pool.setMaxCapacity(maxcap)
pool.setMinCapacity(mincap)
pool.setStatementCacheType(cachetype)
pool.setStatementCacheSize(cachesize)
pool.setTestConnectionsOnReserve(testreserve)
pool.setTestFrequencySeconds(testfreq)
pool.setSecondsToTrustAnIdlePoolConnection(trustidle)
pool.setShrinkFrequencySeconds(shrink)
pool.setTestTableName(testtable)
pool.setInactiveConnectionTimeoutSeconds(inactivetimeout)

# Create driver settings
driver = theresource.getJDBCDriverParams()
driver.setDriverName(drivername)
driver.setUrl(driverurl)
driver.setPassword(driverpassword)
driverprops = driver.getProperties()
userprop = driverprops.createProperty('user')
userprop.setValue(driveruser)

# Set data source target
jdbcresource.addTarget(target)

# Activate changes
save()
activate(block='true')
print '>>>Data source created successfully!'
exit()

