# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# paths
javapath = os.getenv('JAVA_HOME')
fmwpath = os.getenv('MW_HOME')
wlspath = os.getenv('WL_HOME')

# variables
templatefile = wlspath + '/common/templates/wls/wls.jar'
templatename = 'base_domain'
domainname = 'domain3'
domainpath = '/u01/domains/jms/' + domainname
startmode = 'prod'
username = 'weblogic'
password = 'Welcome1'
adminport = 7001
managed1name = 'server1'
managed1port = 7011
managed2name = 'server2'
managed2port = 7012
managed3name = 'server3'
managed3port = 7013
machine1name = 'machine1'
machine2name = 'machine2'
clustername = 'cluster1'
nodemgrport = 5556
host1address = 'host01.example.com'
host2address = 'host02.example.com'


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
set('NMType', 'Plain')
print '>>>Machine ' + machine1name + ' created.'

# create the second machine
cd('/')
create(machine2name, 'Machine')
cd('/Machine/' + machine2name)
create(machine2name, 'NodeManager')
cd('NodeManager/' + machine2name)
set('ListenAddress', host2address)
set('ListenPort', nodemgrport)
set('NMType', 'Plain')
print '>>>Machine ' + machine2name + ' created.'

# Update admin server
cd('/Servers/AdminServer')
set('ListenAddress', host2address)
set('ListenPort', adminport)
set('Machine', machine2name)
print '>>>Admin server updated.'

# create the first managed server
cd('/')
create(managed1name, 'Server')
cd('Servers/' + managed1name)
set('ListenAddress', host1address)
set('ListenPort', managed1port)
set('Machine', machine1name)
print '>>>Server ' + managed1name + ' created.'

# create the second managed server
cd('/')
create(managed2name, 'Server')
cd('Servers/' + managed2name)
set('ListenAddress', host2address)
set('ListenPort', managed2port)
set('Machine', machine2name)
print '>>>Server ' + managed2name + ' created.'

# create the third managed server
cd('/')
create(managed3name, 'Server')
cd('Servers/' + managed3name)
set('ListenAddress', host2address)
set('ListenPort', managed3port)
set('Machine', machine2name)
print '>>>Server ' + managed3name + ' created.'

# create cluster
cd('/')
create(clustername, 'Cluster')
assign('Server', managed1name, 'Cluster', clustername)
assign('Server', managed2name, 'Cluster', clustername)
assign('Server', managed3name, 'Cluster', clustername)
print '>>>Cluster ' + clustername + ' created.'

# write domain to file system
writeDomain(domainpath)
closeTemplate()
print '>>>Domain created successfully at ' + domainpath + '.'

# create boot.properties
os.mkdir(domainpath + '/servers')
os.mkdir(domainpath + '/servers/AdminServer')
os.mkdir(domainpath + '/servers/AdminServer/security')
bootFile = open(domainpath + '/servers/AdminServer/security/boot.properties', 'w')
bootFile.write('username=' + username + '\n')
bootFile.write('password=' + password + '\n')
bootFile.close()
print '>>>Created boot.properties for admin server.'

