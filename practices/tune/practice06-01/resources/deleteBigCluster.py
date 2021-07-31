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


#============ Delete Servers ================
def deleteServers():
	try:
		serverCnt = 3
		portCnt = 7013

		while serverCnt <= 10:
			#Set name for this server
			serverName = 'server' + str(serverCnt)

			cd('/')
			server = getMBean('Servers/' + serverName)
			server.setCluster(None)
			delete(serverName, 'Server')
			print '>>>' + serverName + ' deleted.'
			print ' '
			serverCnt += 1
			portCnt += 1
	except Exception, e:
		print 'Server deletion exception:'
		print e
		dumpStack()
		cancelEdit('y')
		exit()


#============ Main Program ================
print 'Deleting big cluster configuration'

connectWLS('t3://host01:7001')
edit()
startEdit()
deleteServers()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()

