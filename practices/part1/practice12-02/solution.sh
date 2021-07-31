# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------
cp supplies.war /u01/domains/part1/wlsadmin/apps/supplies.war
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST create_dynamic_cluster.py
java weblogic.WLST deploy_app.py
java weblogic.WLST stop_servers.py
java weblogic.WLST start_cluster.py
java weblogic.WLST target_data_source.py
