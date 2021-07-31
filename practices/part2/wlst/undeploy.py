
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script undeploys the named application from the wlsadmin domain's cluster

import sys
import os

#============ Set some variables ===============
app='none'
library='false'
target='cluster1'
#target='AdminServer'

print "This script is obsolete now. We unzip the domain on both machines instead now which is faster and less error prone."
exit()


if len(sys.argv) != 3:
  print "Usage: undeploy.py [d|adminURL] appName"
  exit()

if sys.argv[1] != 'd':
  print "Admin host is " + sys.argv[1]
  host=sys.argv[1]
else:
  host='t3://host01:7001'
  print "Using default admin host of " + host

app=sys.argv[2]
if app == 'AuctionDbLib.war' or app == 'AuctionMemLib.war':
  library='true'
  print "Undeploying library " + app
else:
  print "Undeploying application " + app


#============ Connect to server ================
def unDeployApp():
  print "Undeploying " + app
  try:
    if library == 'false':
      progress=undeploy(app)
      progress.printStatus()
      print '***Application ' + app + ' undeployed successfully***'
    else:
      if app == 'AuctionDbLib.war':
        lib='AuctionLib'
        libSpec='2.0'
        libImpl='1.0'
      else:
        lib='AuctionLib'
        libSpec='1.0'
        libImpl='1.0'
      progress=undeploy(lib, libraryModule='true', libSpecVersion=libSpec, libImplVersion=libImpl)
      progress.printStatus()
      print '***Library ' + lib + '(' + libSpec + ',' + libImpl + ') undeployed successfully***'  
  except:
    print 'Problem undeploying applications'
    print dumpStack()
    exit()


#============ Connect to server ================
def connectWLS(host):
  #WLS Must be running for this script to work
  try:
    connect('weblogic','Welcome1',host)
    print '***Connected successfully***'
  except:
    print 'Domain ' + host + ' must be running first'
    exit()


#============ Main Program ================
connectWLS(host)
unDeployApp()

#Disconnect
disconnect('true')

print 'Completed undeployment'
exit()
