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
templatefile = wlspath + '/common/templates/domains/wls.jar'
#templatefile = wlspath + '/common/templates/wls/wls.jar'
templatename = 'base_domain'
domainname = 'testdynclusterdomain'
domainpath = '/u01/domains/jms/' + domainname
startmode = 'prod'
username = 'weblogic'
password = 'Welcome1'
machine1name = 'machine1'
nodemgrport = 5556
host1address = 'host01.example.com'
adminport = 7001


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

# Update admin server
cd('/Servers/AdminServer')
set('ListenAddress', host1address)
set('ListenPort', adminport)
set('Machine', machine1name)
print '>>>Admin server updated.'

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

