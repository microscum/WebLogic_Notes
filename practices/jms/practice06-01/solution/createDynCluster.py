# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
clusterName = 'dyncluster1'
templateName = clusterName + '-template'
listenPort = 7010
maxServerCount = 4
serverPrefix = 'dyncluster1-'

# Connect to administration server
connect(username, password, url)

# Check if cluster already exists
try:
	cd('/Clusters/' + clusterName)
	print 'The cluster ' + clustereName + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass


edit()
startEdit()

# Create server template
template = cmo.createServerTemplate(templateName)
template.setListenPort(listenPort)
print 'Created server template ' + templateName + '.'

cluster = cmo.createCluster(clusterName)
servers = cluster.getDynamicServers()
servers.setServerNamePrefix(serverPrefix)
servers.setMaximumDynamicServerCount(maxServerCount)
servers.setServerTemplate(template)
servers.setCalculatedMachineNames(true)
print 'Created dynamic cluster ' + clusterName + ' with ' + str(maxServerCount) + ' servers.'

# Activate changes
save()
activate(block='true')
print 'Dynamic cluster created successfully.'

exit()
