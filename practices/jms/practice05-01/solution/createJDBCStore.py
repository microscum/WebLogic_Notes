# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# Modify these values as necessary
url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
storeName = 'JDBCStore1'
targetName = 'server1'
dsName = 'OracleDS1-NoXA'
prefix = 'Store1_'

# Connect to administration server
connect(username, password, url)

# Check if the store already exists
try:
	cd('/JDBCStores/' + storeName)
	print 'The JDBC Store ' + storeName + ' already exists.'
	exit()
except WLSTException:
	pass

print 'Creating new JDBC Store named ' + storeName + '.'

edit()
startEdit()
cd('/')

# Save reference to target server
targetServer = getMBean('/Servers/' + targetName)

# Save reference to target data source
targetDS = getMBean('/SystemResources/' + dsName)

# Create store
jdbcStore = create(storeName, 'JDBCStore')
jdbcStore.setDataSource(targetDS)
jdbcStore.setPrefixName(prefix)

# Set store target
jdbcStore.addTarget(targetServer)

# Activate changes
save()
activate(block='true')
print 'JDBC Store created successfully.'
exit()
