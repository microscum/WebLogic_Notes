
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#============ Configure Overload Protection ================
def configureOverload():
    try:
        #Unset 5-1 configuration (in case it is set) and set configuration needed for 5-3
        mybean = getMBean('/Servers/server2/OverloadProtection/server2')
        mybean.setFailureAction('no-action')
        mybean.setFreeMemoryPercentLowThreshold(20)
        mybean.setFreeMemoryPercentHighThreshold(30)
        mybean.createServerFailureTrigger()

        mybean = getMBean('/Servers/server2/OverloadProtection/server2/ServerFailureTrigger/server2')
        mybean.setMaxStuckThreadTime(600)
        mybean.setStuckThreadCount(0)

        mybean = getMBean('/Servers/server2')
        mybean.setRestartMax(500)
        mybean.setRestartDelaySeconds(2)
        print 'Completed update of domain...'
    except Exception, e:
        print 'Configuration exception:'
        print e
        dumpStack()
        cancelEdit('y')
        exit()


### MAIN START POINT
try:
    #Connect to NodeManager in order to start AdminServer
    nmConnect('weblogic','Welcome1','host01',5556,'wlsadmin','/u01/domains/tune/wlsadmin','plain')

    #Start Admin Server using NodeManager (boot.properties file must exist first)
    nmStart('AdminServer')

    #Connect to AdminServer
    connect('weblogic','Welcome1','host01:7001')

    #Configure 51 and 53 solution prior to starting up managed servers to avoid restart requirement
    edit()
    startEdit()
    configureOverload()
    activate()

    #Start Cluster: cluster name, type, admin server URL, block for completion
    start('cluster1','Cluster','host01:7001',block='true')
except Exception, e:
    print "ERROR... check error messages for cause."
    print e
    dumpStack()
    cancelEdit('y')

#Domain should be started now
#Disconnect
disconnect('true')
exit()

