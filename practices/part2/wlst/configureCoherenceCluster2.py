
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script configures the Coherence cluster solution for practice 16-01

import sys
import os
import weblogic.security.service.URLResource

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

#============ Configure default Coherence cluster ================
def configureCoherence2():
    server1=getMBean('/Servers/server1/CoherenceMemberConfig/server1')
    cluster=getMBean('/Clusters/cluster1')
    cc1=getMBean('/CoherenceClusterSystemResources/CoherenceCluster1')

    print 'Configuring Coherence cluster'
    try:
        #Create ManagedCohoerenceCluster
        cd('/')
        cmo.createCoherenceClusterSystemResource('ManagedCoherenceCluster')
        mcc=getMBean('/CoherenceClusterSystemResources/ManagedCoherenceCluster')

        #Configure Coherence cluster settings
        cd('/CoherenceClusterSystemResources/ManagedCoherenceCluster/CoherenceClusterResource/ManagedCoherenceCluster/CoherenceClusterParams/ManagedCoherenceCluster')
        cmo.setClusteringMode('unicast')
        cmo.setUnicastListenPort(0)

        #Set ManagedCoherenceCluster for cluster1
        cluster.setCoherenceClusterSystemResource(mcc)

        #Target ManagedCoherenceCluster to cluster1
        mcc.addTarget(cluster)

        #Set server1 Coherence properties
        server1.unSet('UnicastListenPort')
        server1.setLocalStorageEnabled(false)
        print ' '
    except Exception, e:
        print 'Coherence configuration exception:'
        print e
        print ' '

#============ Main Program ================
print 'Updating domain Coherence configuration'

connectWLS('t3://host01:7001')

edit()
startEdit()
configureCoherence2()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
