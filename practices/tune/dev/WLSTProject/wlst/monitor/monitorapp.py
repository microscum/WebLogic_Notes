
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

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

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
    #Switch to the domainRuntime tree
    domainRuntime()
    cd('/ServerRuntimes')
    servers=domainRuntimeService.getServerRuntimes()

    rc=os.system('clear')
    print ''
    print '---------------------------------------------'
    print 'Server\tSessions\tRequests'

    #Loop through the servers
    for server in servers:
      #Skip AdminServer because the web app is not deployed there
      if server.getName() == 'AdminServer':
        continue
      cd('/ServerRuntimes/' + server.getName())
      webModule = getMBean('ApplicationRuntimes/' + appName + '/ComponentRuntimes/' + server.getName() + '_/' + appWebRoot)
      sessions = str(webModule.getOpenSessionsCurrentCount())
      appWM = getMBean('ApplicationRuntimes/' + appName + '/WorkManagerRuntimes/' + wmName)
      invokeCount = str(appWM.getCompletedRequests())
      print server.getName() + '\t' + sessions + '\t\t' + invokeCount

    print '---------------------------------------------'	
    jythontime.sleep(15)
  except Exception, e:
    print 'Exception: ' + e
	
disconnect()

