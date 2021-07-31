# Creates a cluster as if you followed the directions
# in the practice "Configuring a Cluster"
#
# By: ST Curriculum Development Team
# Version 1.1
# Last updated: May 22, 2013
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
clustername = 'cluster3'
s1 = 'server3'
s2 = 'server4'
s3 = 'server5'
s4 = 'server6'
m1 = 'machine1'
m2 = 'machine2'
addr1 = 'host01.example.com'
addr2 = 'host02.example.com'
port1 = 7013
port2 = 7015


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

# Go get machines to use later
cd('/Machines')
cd(m1)
mach1 = cmo
cd('/Machines')
cd(m2)
mach2 = cmo

# Create a cluster 
cd('/')
thecluster = cmo.createCluster(clustername)
print '>>>Created cluster ' + clustername + '.'

# Create managed servers
cd('/')
create(s1, 'Server')
cd('Servers/' + s1)
set('ListenAddress', addr1)
set('ListenPort', port1)
set('Machine', mach1)
set('Cluster', thecluster)
print '>>>' + s1 + ' created.'

cd('/')
create(s2, 'Server')
cd('Servers/' + s2)
set('ListenAddress', addr2)
set('ListenPort', port1)
set('Machine', mach2)
set('Cluster', thecluster)
print '>>>' + s2 + ' created.'

cd('/')
create(s3, 'Server')
cd('Servers/' + s3)
set('ListenAddress', addr1)
set('ListenPort', port2)
set('Machine', mach1)
set('Cluster', thecluster)
print '>>>' + s3 + ' created.'

cd('/')
create(s4, 'Server')
cd('Servers/' + s4)
set('ListenAddress', addr2)
set('ListenPort', port2)
set('Machine', mach2)
set('Cluster', thecluster)
print '>>>' + s4 + ' created.'


# Save and activate the changes
save()
activate(block='true')
print '>>>Cluster and its servers created successfully.'

exit()
