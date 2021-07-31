# Creates a new domain in which you will configure an admin port
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: May 21, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# get operating system (for vars)
import os

# paths
javapath = os.getenv('JAVA_HOME')
# Expected: '/u01/app/jdk'
wlspath = os.getenv('WL_HOME')
# Expected: '/u01/app/fmw/wlserver'

# variables
templatefile = wlspath + '/common/templates/wls/wls.jar'
templatename = 'base_domain'
domainname = 'wlsadmin2'
domainpath = '/u01/domains/part1/' + domainname
startmode = 'prod'
username = 'weblogic'
password = 'Welcome1'
managed1name = 'server1a'
managed2name = 'server2a'
machine1name = 'machine1a'
machine2name = 'machine2a'
nodemgrport = 6665
clustername = 'cluster1a'
host1address = 'host01.example.com'
host2address = 'host02.example.com'
adminport = 8001
managedport = 8011


# Load the base template
readTemplate(templatefile)
print '>>>Domain template loaded: ' + templatefile

# Set domain options
setOption('JavaHome',javapath)
setOption('ServerStartMode',startmode)
setOption('OverwriteDomain','true')

# Set admin credentials
cd('/Security/' + templatename + '/User/' + username)
cmo.setPassword(password)
print '>>>Admin user created.'

# create the first machine
cd('/')
create(machine1name, 'Machine')
cd('/Machine/' + machine1name)
create(machine1name, 'NodeManager')
cd('NodeManager/' + machine1name)
set('ListenAddress', host1address)
set('ListenPort', nodemgrport)
print '>>>' + machine1name + ' created.'

# create the second machine
cd('/')
create(machine2name, 'Machine')
cd('/Machine/' + machine2name)
create(machine2name, 'NodeManager')
cd('NodeManager/' + machine2name)
set('ListenAddress', host2address)
set('ListenPort', nodemgrport)
print '>>>' + machine2name + ' created.'

# Update admin server
cd('/Servers/AdminServer')
set('ListenAddress', host1address)
set('ListenPort', adminport)
set('Machine', machine1name)
print '>>>Admin server updated.'

# create first managed server
cd('/')
create(managed1name, 'Server')
cd('Servers/' + managed1name)
set('ListenAddress', host1address)
set('ListenPort', managedport)
set('Machine', machine1name)
print '>>>' + managed1name + ' created.'

# create second managed server
cd('/')
create(managed2name, 'Server')
cd('Servers/' + managed2name)
set('ListenAddress', host2address)
set('ListenPort', managedport)
set('Machine', machine2name)
print '>>>' + managed2name + ' created.'

# create the cluster & assign servers
cd('/')
create(clustername, 'Cluster')
cd('/')
assign('Server', managed1name, 'Cluster', clustername)
assign('Server', managed2name, 'Cluster', clustername)
print '>>>' + clustername + ' created and managed servers added to it.'

# Write domain to file system
writeDomain(domainpath)
closeTemplate()
print '>>>Domain created successfully at ' + domainpath + '.'
