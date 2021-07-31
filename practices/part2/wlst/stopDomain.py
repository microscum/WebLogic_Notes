
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Make sure both NodeManagers are started on each machine first

try:
  #Connect to AdminServer
  connect('weblogic','Welcome1','t3://host01:7001')

  #Shut down Cluster: cluster name, type, ignoreSessions, secs to allow sessions to end, block until finished
  shutdown('cluster1','Cluster','true',5,block='true')

  #Shut down Admin Server
  shutdown()
  
except:
  print "ERROR... check error messages for cause."

#Domain should be stopped now
exit()

