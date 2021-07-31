
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
  #Connect to NodeManager in order to start AdminServer
  nmConnect('weblogic','Welcome1','host01',5556,'wlsadmin','/u01/domains/part2/wlsadmin','plain')

  #Start Admin Server using NodeManager (boot.properties file must exist first)
  nmStart('AdminServer')

  #Connect to AdminServer
  connect('weblogic','Welcome1','host01:7001')

  #Start Cluster: cluster name, type, admin server URL, block for completion
  start('cluster1','Cluster','host01:7001',block='true')
except:
  print "ERROR... check error messages for cause."

#Domain should be started now
exit()

