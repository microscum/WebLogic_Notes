
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
dsName = 'jdbc.Auction2'

# Connect to administration server
connect(username, password, url)

# Check if data source exists
try:
    cd('/JDBCSystemResources/' + dsName)
except WLSTException:
    print 'The JDBC Data Source ' + dsName + ' does not exist.'
    exit()

print 'Deleting JDBC Data Source named ' + dsName + '.'

edit()
startEdit()
cd('/')

# Remove data source
delete(dsName,'JDBCSystemResource')

# Activate changes
save()
activate(block='true')
print 'Data Source deleted successfully.'
exit()
