# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. 
# --    It is NOT supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------
#!/bin/sh

#Delete domain if it already exists
rm -rf /u01/domains/tshoot/wlsadmin

source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST create_domain.py
