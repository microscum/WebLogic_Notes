# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

host1 = 'host01.example.com'
host2 = 'host02.example.com'

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


#============ Create Servers and Assign to Cluster ================
def createServers():
	try:
		serverCnt = 3
		portCnt = 7013

		cluster = getMBean('/Clusters/cluster1')
		machine1 = getMBean('/Machines/machine1')
		machine2 = getMBean('/Machines/machine2')

		while serverCnt <= 12:
			#Set name and port for this server
			serverName = 'server' + str(serverCnt)
			serverPort = portCnt

			#Set host and machine for this server
			if serverCnt % 2 != 0:
				host = host1
				machine = machine1
			else:
				host = host2
				machine = machine2 

			cd('/')
			create(serverName, 'Server')
			cd('Servers/' + serverName)
			set('ListenAddress', host)
			set('ListenPort', serverPort)
			set('Machine', machine)
			set('Cluster', cluster)
			print '>>>' + serverName + ":" + host + ":" + machine.getName() + ' created.'
			print ' '
			serverCnt += 1
			portCnt += 1
	except Exception, e:
		print 'Server creation exception:'
		print e
		dumpStack()
		cancelEdit('y')
		exit()


#============ Main Program ================
print 'Creating big cluster configuration'

connectWLS('t3://host01:7001')
edit()
startEdit()
createServers()
activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()

