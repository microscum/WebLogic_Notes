
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script deploys the named application to the wlsadmin domain's cluster

import sys
import os

#============ Set some variables ===============
appname=''
apppath=''
library='false'
target='cluster1'
#target='AdminServer'

print "This script is obsolete now. We use weblogic.Deployer instead because it executes faster."
exit()

#print len(sys.argv)

if len(sys.argv) != 3:
  print "Usage: deploy.py [d|adminURL] appName"
  exit()

if sys.argv[1] != 'd':
  print "Admin host is " + sys.argv[1]
  host=sys.argv[1]
else:
  host='t3://host01:7001'
  print "Using default admin host of " + host

if sys.argv[2]:
  if "orig" in sys.argv[2]:
    appname=sys.argv[2].replace('orig/','')
    apppath='/practices/part2/apps/orig/' + appname
  elif "solution" in sys.argv[2]:
    appname=sys.argv[2].replace('solution/','')
    apppath='/practices/part2/apps/solution/' + appname
  else:
    print "ERROR: Deployent must be in orig or solution folder"
    exit()
  
  print "Deploying " + sys.argv[2]
  
  print "App full name is: " + apppath
  if appname == 'AuctionDbLib.war' or appname == 'AuctionMemLib.war':
    library='true'
else:
  print "Application is not set!"
  exit()


#============ Connect to server ================
def deployApp():
  try:
    if library == 'false':
      deploy(appName=appname, path=apppath, targets=target)
      print '***Application deployment successful***'
    else:
      deploy('AuctionLib', path=apppath, targets=target, libraryModule='true')
      print '***Library deployment successful***'
  except:
    print 'Problem deploying application'
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
deployApp()

#Disconnect
disconnect('true')

print 'Completed deployment'
exit()
