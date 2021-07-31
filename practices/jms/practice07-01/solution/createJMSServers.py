# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host02:7001'
username = 'weblogic'
password = 'Welcome1'

serverName1 = 'server1'
serverName2 = 'server2'
serverName3 = 'server3'

dsName = 'OracleDS1-NoXA'

storeName1 = 'JDBCStore1'
storeName2 = 'JDBCStore2'
storeName3 = 'JDBCStore3'

jmsServerName1 = 'JMSServer1'
jmsServerName2 = 'JMSServer2'
jmsServerName3 = 'JMSServer3'

# Connect to administration server
connect(username, password, url)

edit()
startEdit()

# Save references to servers
server1 = getMBean('/Servers/' + serverName1)
server2 = getMBean('/Servers/' + serverName2)
server3 = getMBean('/Servers/' + serverName3)

# Save reference to data source
jdbcSystemResource = getMBean('/JDBCSystemResources/' + dsName)


# Create first Store
print 'Creating new Persistent Store named ' + storeName1 + '.'
jdbcStore1 = create(storeName1, 'JDBCStore')
jdbcStore1.setDataSource(jdbcSystemResource)
jdbcStore1.setPrefixName(storeName1)
jdbcStore1.addTarget(server1)

# Create second Store
print 'Creating new Persistent Store named ' + storeName2 + '.'
jdbcStore2 = create(storeName2, 'JDBCStore')
jdbcStore2.setDataSource(jdbcSystemResource)
jdbcStore2.setPrefixName(storeName2)
jdbcStore2.addTarget(server2)

# Create third Store
print 'Creating new Persistent Store named ' + storeName3 + '.'
jdbcStore3 = create(storeName3, 'JDBCStore')
jdbcStore3.setDataSource(jdbcSystemResource)
jdbcStore3.setPrefixName(storeName3)
jdbcStore3.addTarget(server3)

# Create first JMS Server
print 'Creating new JMS Server named ' + jmsServerName1 + '.'
jmsServer1 = create(jmsServerName1, 'JMSServer')
jmsServer1.setPersistentStore(jdbcStore1)
jmsServer1.addTarget(server1)

# Create second JMS Server
print 'Creating new JMS Server named ' + jmsServerName2 + '.'
jmsServer2 = create(jmsServerName2, 'JMSServer')
jmsServer2.setPersistentStore(jdbcStore2)
jmsServer2.addTarget(server2)

# Create third JMS Server
print 'Creating new JMS Server named ' + jmsServerName3 + '.'
jmsServer3 = create(jmsServerName3, 'JMSServer')
jmsServer3.setPersistentStore(jdbcStore3)
jmsServer3.addTarget(server3)

# Activate changes
save()
activate(block='true')
print 'All JMS resources created successfully.'

exit()
