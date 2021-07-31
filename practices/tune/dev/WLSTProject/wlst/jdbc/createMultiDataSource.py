
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
dsName = 'AuctionDBMultiDataSource'
dsJNDIName = 'AuctionDBMultiDataSource'
targetName = 'cluster1'

# Connect to administration server
connect(username, password, url)

# Check if data source already exists
try:
    cd('/JDBCSystemResources/' + dsName)
    print 'The JDBC Data Source ' + dsName + ' already exists.'
    exit()
except WLSTException:
    pass

print 'Creating new JDBC Multi Data Source named ' + dsName + '.'

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

# Set data source members
jdbcResourceParameters.setAlgorithmType('Failover')
jdbcResourceParameters.setDataSourceList('jdbc.Auction,jdbc.Auction2')

# Set data source target
jdbcSystemResource.addTarget(targetServer)

# Activate changes
save()
activate(block='true')
print 'Multi Data Source created successfully.'
exit()
