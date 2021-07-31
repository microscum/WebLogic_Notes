
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script resets the Coherence cluster for practice 16-02 back to its starting point

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
def resetCoherence2():
    server1=getMBean('/Servers/server1/CoherenceMemberConfig/server1')
    cluster=getMBean('/Clusters/cluster1')
    cc1=getMBean('/CoherenceClusterSystemResources/CoherenceCluster1')
    mcc=getMBean('/CoherenceClusterSystemResources/ManagedCoherenceCluster')

    print 'Resetting Coherence default cluster'
    try:
        #Remove all Coherence clusters from cluster1
        cluster.setCoherenceClusterSystemResource(None)

        #Remove ManagedCoherenceCluster from cluster1
        mcc.removeTarget(cluster)

        #Set default CoherenceCluster1 as cluster for cluster1
        cluster.setCoherenceClusterSystemResource(cc1)

        #Target CoherenceCluster1 to cluster1
        cc1.addTarget(cluster)

        #Delete ManagedCoherenceCluster
        cd('/')
        cmo.destroyCoherenceClusterSystemResource(mcc)

        #Reset local storage for server1
        server1.setLocalStorageEnabled(true)
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
resetCoherence2()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
