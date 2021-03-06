
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script undeploys all applications from the domain

import sys
import os

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
    
#============ Set some variables ===============
target='cluster1'
#target='AdminServer'
undeploylist=['_auto_generated_ear_',
              'ShoppingCart',
              'ShoppingCart.war',
              'AuctionWebAppSec.war',
              'AuctionWebApp.war',
              'SimpleAuctionWebAppDbSec.war',
              'SimpleAuctionWebAppDb.war',
              'SimpleAuctionWebAppDb',
              'SimpleAuctionWebAppDb1.war',
              'SimpleAuctionWebAppDb1',
              'SimpleAuctionWebAppDb2.war',
              'SimpleAuctionWebAppDb2',
              'SimpleAuctionWebAppSec.war',
              'SimpleAuctionWebApp.war',
              'AuctionWebApp#v1',
              'AuctionWebApp#v2' ]

if len(sys.argv) != 2:
  print "Usage: undeployall.py [d|adminURL]"
  exit()

if sys.argv[1] != 'd':
  print "Admin host is " + sys.argv[1]
  host=sys.argv[1]
else:
  host='t3://host01:7001'
  print "Using default admin host of " + host


#============ Connect to server ================
def unDeployApps():
  progress=None
  print "Undeploying all course applications"
  try:
    for i in cmo.getAppDeployments():
      print "Application=" + i.getName()
      for app in undeploylist:
        if i.getName() == app: 
          progress=undeploy(app, timeout=360000)
          progress.printStatus()
          print '***App ' + app + ' undeployed successfully***'
          break
  except:
    print 'Problem undeploying applications'
    print dumpStack()
    exit()

  try:
    #After all apps are undeployed, then it is safe to undeploy libraries
    cd('serverConfig:/Libraries/AuctionLib#2.0@1.0')
    progress=undeploy('AuctionLib', libraryModule='true', libSpecVersion='2.0', libImplVersion='1.0', timeout=360000)
    progress.printStatus()
  except:
    pass

  try:
    cd('serverConfig:/Libraries/AuctionLib#1.0@1.0')
    progress=undeploy('AuctionLib', libraryModule='true', libSpecVersion='1.0', libImplVersion='1.0', timeout=360000)
    progress.printStatus()
  except:
    pass


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
unDeployApps()

#Disconnect
disconnect('true')

print 'Completed undeployment'
exit()
