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
listenAddress1 = '192.0.2.21'
serverName2 = 'server2'
listenAddress2 = '192.0.2.22'
serverName3 = 'server3'
listenAddress3 = '192.0.2.23'

# Connect to administration server
connect(username, password, url)

edit()
startEdit()

# Update server1
print 'Updating server ' + serverName1 + '.'
theServer = getMBean('/Servers/' + serverName1)
theServer.setListenAddress(listenAddress1)
theServer.setAutoMigrationEnabled(true)

# Update server2
print 'Updating server ' + serverName2 + '.'
theServer = getMBean('/Servers/' + serverName2)
theServer.setListenAddress(listenAddress2)
theServer.setAutoMigrationEnabled(true)

# Update server3
print 'Updating server ' + serverName3 + '.'
theServer = getMBean('/Servers/' + serverName3)
theServer.setListenAddress(listenAddress3)
theServer.setAutoMigrationEnabled(true)

# Activate changes
save()
activate(block='true')
print 'Servers updated successfully.'

exit()
