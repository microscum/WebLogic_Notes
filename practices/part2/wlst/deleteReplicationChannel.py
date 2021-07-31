
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

#============ Delete Channel ================
def deleteChannel():
    try:
        #Set replication channel name on cluster
        cluster=getMBean('/Clusters/cluster1')
        cluster.setReplicationChannel('')
        #cluster.unSet('replicationChannel')
        #cluster.unSet('ReplicationChannel')
        cluster.unSet('RemoteClusterAddress')
        cluster.setClusterType('none')        

        #Delete channel on server1
        server=getMBean('/Servers/server1')
        server.destroyNetworkAccessPoint(getMBean('/Servers/server1/NetworkAccessPoints/ReplicationChannel'))

        #Delete channel on server2
        server=getMBean('/Servers/server2')
        server.destroyNetworkAccessPoint(getMBean('/Servers/server2/NetworkAccessPoints/ReplicationChannel'))
    except Exception, e:
        print 'Replication channel deletion exception:'
        print e 


#============ Delete Replication Groups ================
def deleteRepGroup():
    try:
        server=getMBean('/Servers/server1')
        server.unSet('PreferredSecondaryGroup')
        server.unSet('ReplicationGroup')
        server=getMBean('/Servers/server2')
        server.unSet('PreferredSecondaryGroup')
        server.unSet('ReplicationGroup')
    except Exception, e:
        print 'Replication group deletion exception:'
        print e 


#============ Main Program ================
print 'Deleting replication configuration'

connectWLS('t3://host01:7001')
edit()
startEdit()
deleteChannel()
deleteRepGroup()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
