
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
def configureCoherence():
    coh=getMBean('/CoherenceClusterSystemResources/CoherenceCluster1/CoherenceClusterResource/CoherenceCluster1/CoherenceClusterParams/CoherenceCluster1')

    print 'Configuring Coherence default cluster'
    try:
        coh.setClusteringMode('multicast')
        coh.setMulticastListenAddress('224.12.1.0')
        coh.setMulticastListenPort(12100)
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
configureCoherence()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
