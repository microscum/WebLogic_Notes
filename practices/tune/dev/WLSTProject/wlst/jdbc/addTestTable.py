
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
dsName = 'jdbc.Auction'
dsJNDIName = 'jdbc.Auction'
targetName = 'cluster1'

# Connect to administration server
connect(username, password, url)

# Check if data source exists
try:
    cd('/JDBCSystemResources/' + dsName)
    print 'The JDBC Data Source ' + dsName + ' exists.'
    
    print 'Updating configuration for JDBC Data Source named ' + dsName + '.'

    edit()
    startEdit()
    cd('/')
    
    jdbcSystemResource = getMBean('/JDBCSystemResources/' + dsName)
    jdbcResource = jdbcSystemResource.getJDBCResource()
    connectionPool = jdbcResource.getJDBCConnectionPoolParams()
    connectionPool.setTestConnectionsOnReserve(true)
    connectionPool.setTestTableName('SQL SELECT 1 FROM DUAL')
    
    # Activate changes
    save()
    activate(block='true')
    print 'Data Source updated successfully.'
    exit()
except WLSTException:
    print 'Data source does not exist'
    exit()
