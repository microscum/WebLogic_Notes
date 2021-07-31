# Creates a dynamic cluster as if you followed the directions
# in the dynamic cluster practice
#
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: April 25, 2013
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
clustername = 'cluster2'
#listenaddress = '192.0.2.1${id}'
listenport = 7099
ssllistenport = 8099
maxservercount = 4
serverprefix = 'cluster2server-'
templatename = serverprefix + 'Template'

# Connect to administration server
connect(username, password, url)

# Check if cluster already exists
try:
	cd('/Clusters/' + clustername)
	print '>>>The cluster ' + clustername + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass


edit()
startEdit()

# Create server template
cd('/')
template = cmo.createServerTemplate(templatename)
cd('/ServerTemplates/' + templatename)
cmo.setListenPort(listenport)
cmo.setListenPortEnabled(true)
cd('SSL/' + templatename)
cmo.setListenPort(ssllistenport)
cmo.setEnabled(false)

print '>>>Created server template ' + templatename + '.'

# Create dynamic cluster based on the template
cd('/')
cluster = cmo.createCluster(clustername)
servers = cluster.getDynamicServers()
servers.setServerNamePrefix(serverprefix)
servers.setMaximumDynamicServerCount(maxservercount)
servers.setServerTemplate(template)
servers.setCalculatedMachineNames(true)
print '>>>Created dynamic cluster ' + clustername + ' with ' + str(maxservercount) + ' servers.'

# Save and activate the changes
save()
activate(block='true')
print '>>>Dynamic cluster created successfully.'

exit()
