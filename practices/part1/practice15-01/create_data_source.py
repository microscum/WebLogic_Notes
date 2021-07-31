# Creates the TLog data source as if you followed the instructions for 
# the practice "Configuring Transaction Persistence"
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: May 23, 2013
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
dsname = 'tlogdatasource1'
jndiname = 'tlogds1'
clustername = 'cluster2'

drivername = 'oracle.jdbc.OracleDriver'
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

print '>>>Creating a new generic JDBC data source named ' + dsname + '.'

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
jdbcresourceparams.setGlobalTransactionsProtocol('None')

# Create connection pool
pool = theresource.getJDBCConnectionPoolParams()
pool.setTestTableName(testtable)

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

