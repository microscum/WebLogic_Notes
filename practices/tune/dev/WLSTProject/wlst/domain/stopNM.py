
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

import os

host=os.environ['HOSTNAME']

try:
  #Connect to NodeManager in order to stop it
  nmConnect('weblogic','Welcome1',host,5556,'wlsadmin')
  stopNodeManager()

except:
  print "ERROR... check error messages for cause."

#NM should be stopped now
exit()



