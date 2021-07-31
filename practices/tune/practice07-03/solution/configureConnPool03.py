# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
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


#============ Configure Connection Pool ================
def configureConnPool():
    try:
        mybean = getMBean('/JDBCSystemResources/jdbc/AuctionDB/JDBCResource/jdbc.AuctionDB/JDBCConnectionPoolParams/jdbc.AuctionDB')
        mybean.setMaxCapacity(15)
        mybean.setMinCapacity(15)
        mybean.setInitialCapacity(15)
        mybean.setStatementCacheSize(15)
        mybean.setPinnedToThread(true)
    except Exception, e:
        print 'Configuration exception:'
        print e
        dumpStack()
        cancelEdit('y')
        exit()


#============ Main Program ================
print 'Creating Connection Pool configuration'

connectWLS('t3://host01:7001')
edit()
startEdit()
configureConnPool()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'

