# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST create_channels.py
cp /practices/part1/practice10-01/update/benefits.war /u01/domains/part1/wlsadmin/apps/benefits.war
java weblogic.WLST deploy_app.py
