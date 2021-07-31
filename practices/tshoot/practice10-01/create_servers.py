# Creates two new servers
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 7, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
newserver1 = 'server3'
newserver2 = 'server4'
machine1 = 'machine1'
machine2 = 'machine2'
newserver1addr = 'host01.example.com'
newserver2addr = 'host02.example.com'
newserverport = 7013
clustername = 'cluster1'


# Connect to administration server
connect(username, password, url)

# Check if each server already exists
try:
	cd('/Servers/' + newserver1)
	print '>>>The server named ' + newserver1 + ' already exists.'
	exit()
except WLSTException:
	pass

try:
	cd('/Servers/' + newserver2)
	print '>>>The server named ' + newserver2 + ' already exists.'
	exit()
except WLSTException:
	pass


# start an edit session
edit()
# lock the configuration
startEdit()

# go to the root
cd('/')

# Save a reference to each machine
machine1ref = getMBean('/Machines/' + machine1)
machine2ref = getMBean('/Machines/' + machine2)

# Save a reference to the cluster
clusterref = getMBean('/Clusters/' + clustername)

# Create the first new server
print '>>>Creating a new server named ' + newserver1 + '.'
server1ref = create(newserver1, 'Server')
server1ref.setListenAddress(newserver1addr)
server1ref.setListenPort(newserverport)
server1ref.setMachine(machine1ref)
server1ref.setCluster(clusterref)

# Create the second new server
print '>>>Creating a new server named ' + newserver2 + '.'
server2ref = create(newserver2, 'Server')
server2ref.setListenAddress(newserver2addr)
server2ref.setListenPort(newserverport)
server2ref.setMachine(machine2ref)
server2ref.setCluster(clusterref)

# Activate changes
save()
activate(block='true')
print '>>>Servers created successfully!'
exit()

