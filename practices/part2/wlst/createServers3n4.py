
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

clustername='cluster2'

#============ Connect to server ================
def connectWLS(host):
  #WLS Must be running for this script to work
  try:
    connect('weblogic','Welcome1',host)
    print '***Connected successfully***'
  except:
    print 'Domain ' + host + ' must be running first'
    exit()


def createCluster2():
  # Go get machines to use later
  mach1=getMBean('/Machines/machine1')
  mach2=getMBean('/Machines/machine2')

  #Create cluster2
  cd('/')
  cluster2 = cmo.createCluster(clustername)
  cd('/Clusters/cluster2')
  cmo.setClusterMessagingMode('unicast')
  print 'Created cluster ' + clustername + '.'
  print ' '

  #Create servers
  i=0
  print 'creating servers'
  servers = ['server3','server4']
  addresses = ['host01.example.com','host02.example.com']
  ports = [7013,7014]
  machines = [mach1,mach2]
  for server in servers:
    try:
      print 'creating server: ' + server
      cd('/')
      create(server, 'Server')
      cd('Servers/' + server)
      set('ListenAddress', addresses[i])
      set('ListenPort', ports[i])
      set('Machine', machines[i])
      set('Cluster', cluster2)
      print 'Server ' + server + ' created.'
      i += 1
      print ' '
    except:
      print 'Cluster creation exception'
      dumpstack()
      cancelEdit()
      exit()


#============ Main Program ================
print 'Updating domain with configuration for Coherence*Web practice.'

#Connect to Admin
connectWLS('t3://host01:7001')

#Ensure config doesn't already exist
try:
	cd('/Clusters/' + clustername)
	print '>>>The cluster ' + clustername + ' already exists. Exiting...'
	exit()
except WLSTException:
	pass

edit()
startEdit()

createCluster2()

activate()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()



