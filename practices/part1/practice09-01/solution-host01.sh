# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------
cp -f nodemanager.properties.host01 /u01/domains/part1/wlsadmin/nodemanager/nodemanager.properties
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST update_machines.py
