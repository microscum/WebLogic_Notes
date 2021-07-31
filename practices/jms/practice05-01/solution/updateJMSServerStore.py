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
jmsServerName = 'JMSServer1'
storeName = 'JDBCStore1'

# Connect to administration server
connect(username, password, url)

# Check if JMS Server exists
try:
	cd('/JMSServers/' + jmsServerName)
except WLSTException:
	print 'The JMS Server ' + jmsServerName + ' does not exist.'
	exit()

print 'Updating JMS Server named ' + jmsServerName + '.'

edit()
startEdit()
cd('/')

# Update JMS Server
jmsServer = getMBean('/JMSServers/' + jmsServerName)
jmsServer.setPersistentStore(getMBean('/JDBCStores/' + storeName))

# Activate changes
save()
activate(block='true')
print 'JMS Server updated successfully.'
exit()
