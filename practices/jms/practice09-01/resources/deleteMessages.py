# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

# Modify these values as necessary
url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
serverName1 = 'server1'
jmsServerName = 'JMSServer1'
moduleName = 'JMSModule1'
destName1 = 'Queue1'
destName2 = 'ErrorQueue1'

# Connect to administration server
connect(username, password, url)

domainRuntime()

print 'Deleting all messages on ' + destName1
dest = getMBean('/ServerRuntimes/' + serverName1 + '/JMSRuntime/' + serverName1 + '.jms/JMSServers/' + jmsServerName + '/Destinations/' + moduleName + '!' + destName1)
dest.deleteMessages('')

print 'Deleting all messages on ' + destName2
dest = getMBean('/ServerRuntimes/' + serverName1 + '/JMSRuntime/' + serverName1 + '.jms/JMSServers/' + jmsServerName + '/Destinations/' + moduleName + '!' + destName2)
dest.deleteMessages('')

exit()
