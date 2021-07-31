# Creates the network channels as if you followed the instructions for the
# practice "Configuring a Network Channel"
#
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

# variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
s1 = 'server1'
s2 = 'server2'
chan1 = 'httpchannel-1'
chan2 = 'httpchannel-2'
addr1 = 'host01.example.com'
addr2 = 'host02.example.com'
port = 4000
prot = 'http'

# Connect to administration server
connect(username, password, url)

# Check if the first channel already exists
try:
	cd('/Servers/' + s1 + '/NetworkAccessPoints/' + chan1)
	print '>>>The network channel ' + chan1 + ' already exists.'
	exit()
except WLSTException:
	pass

# Check if the second channel already exists
try:
	cd('/Servers/' + s2 + '/NetworkAccessPoints/' + chan2)
	print '>>>The network channel ' + chan2 + ' already exists.'
	exit()
except WLSTException:
	pass

# start an edit session
edit()

# lock the configuration
startEdit()


# create first channel
print '>>>Creating channel called ' + chan1 + ' on ' + s1 + '. '
cd('/Servers/' + s1)
cmo.createNetworkAccessPoint(chan1)

cd('NetworkAccessPoints/' + chan1)
cmo.setProtocol(prot)
cmo.setListenAddress(addr1)
cmo.setListenPort(port)
cmo.setEnabled(true)
cmo.setHttpEnabledForThisProtocol(true)
cmo.setTunnelingEnabled(false)
cmo.setOutboundEnabled(false)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)

# create second channel
print '>>>Creating channel called ' + chan2 + ' on ' + s2 + '. '
cd('/Servers/' + s2)
cmo.createNetworkAccessPoint(chan2)

cd('NetworkAccessPoints/' + chan2)
cmo.setProtocol(prot)
cmo.setListenAddress(addr2)
cmo.setListenPort(port)
cmo.setEnabled(true)
cmo.setHttpEnabledForThisProtocol(true)
cmo.setTunnelingEnabled(false)
cmo.setOutboundEnabled(false)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)

# Activate changes
save()
activate(block='true')
print '>>>Channels created successfully!'


# exit WLST
exit()
