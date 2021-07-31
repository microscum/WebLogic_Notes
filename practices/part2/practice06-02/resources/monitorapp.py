
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

import sys
import time as jythontime

url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
appName = 'SimpleAuctionWebApp'
appWebRoot = 'SimpleAuctionWebApp'
wmName = 'default'

try:
  #Connect to the Admin Server
  connect(username, password, url)
except:
  print 'Server not available.'
  exit()

# Loop indefinitely
while 1:
  sessions = '-'
  invokeCount = '-'

  # Connect to each managed server's runtime MBeans and retrieve session and request counts
  # via the main domain's domainRuntime MBean
  try:
    #TODO: Switch to the domainRuntime tree
    #TODO: Navigate to the ServerRuntimes MBean
    #TODO: Create a variable and store a list of server runtimes in it

    rc=os.system('clear')
    print ''
    print '---------------------------------------------'
    print 'Server\tSessions\tRequests'

    #Loop through the servers
    for server in servers:
      #TODO: Skip AdminServer because the web app is not deployed there
      #TODO: Navigate to the server runtime of the current server entry represented by your variable
      #TODO: Get the MBean associated with the runtime of the SimpleAuctionWebApp application
      #TODO: Use the SimpleAuctionWebApp MBean to get the current open session count for the server
      #TODO: Get the MBean for the default work manager used by the application and store it in a var
      #TODO: Use the work manager MBean to get the current number of completed requests on the server
      print server.getName() + '\t' + sessions + '\t\t' + invokeCount

    print '---------------------------------------------'	
    jythontime.sleep(15)
  except Exception, e:
    print 'Exception: ' + e
	
disconnect()

