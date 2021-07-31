
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

#============ Connect to server ================
def connectWLS(host):
    #WLS Must be running for this script to work
    try:
        connect('weblogic','Welcome1',host)
        print '***Connected successfully***'
    except:
        print 'Domain ' + host + ' must be running first'
        exit()

#============ Create Channel ================
def createChannel():
    try:
        #Create channel on server1
        server=getMBean('/Servers/server1')
        server.createNetworkAccessPoint('ReplicationChannel')
        channel=getMBean('/Servers/server1/NetworkAccessPoints/ReplicationChannel')
        channel.setProtocol('t3')
        channel.setListenAddress('host01')
        channel.setListenPort(5000)
        channel.setEnabled(true)
        channel.setHttpEnabledForThisProtocol(true)
        channel.setTunnelingEnabled(false)
        channel.setOutboundEnabled(true)
        channel.setTwoWaySSLEnabled(false)
        channel.setClientCertificateEnforced(false)

        server=getMBean('/Servers/server2')
        server.createNetworkAccessPoint('ReplicationChannel')
        channel=getMBean('/Servers/server2/NetworkAccessPoints/ReplicationChannel')
        channel.setProtocol('t3')
        channel.setListenAddress('host02')
        channel.setListenPort(5000)
        channel.setEnabled(true)
        channel.setHttpEnabledForThisProtocol(true)
        channel.setTunnelingEnabled(false)
        channel.setOutboundEnabled(true)
        channel.setTwoWaySSLEnabled(false)
        channel.setClientCertificateEnforced(false)

        #Set replication channel name on cluster
        cluster=getMBean('/Clusters/cluster1')
        cluster.setReplicationChannel('ReplicationChannel')
    except Exception, e:
        print 'Replication channel creation exception:'
        print e 

#============ Delete Replication Groups ================
def createRepGroup():
    try:
        server=getMBean('/Servers/server1')
        server.setReplicationGroup('host01')
        server.setPreferredSecondaryGroup('host02')
        server=getMBean('/Servers/server2')
        server.setReplicationGroup('host02')
        server.setPreferredSecondaryGroup('host01')
    except Exception, e:
        print 'Replication group creation exception:'
        print e 

#============ Main Program ================
print 'Creating replication configuration'

connectWLS('t3://host01:7001')
edit()
startEdit()
createChannel()
createRepGroup()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
