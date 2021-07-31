#!/bin/bash
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

# copy the new (good) version of the application from the current practice directory to the apps directory
cp supplies.war.good /u01/domains/tshoot/wlsadmin/apps/supplies.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to redeploy the app
java weblogic.WLST deploy_app.py

# call WLST to disable debug flags
java weblogic.WLST disable_debug.py

# call WLST to shut down the new servers
java weblogic.WLST shutdown.py

# call WLST to delete the new servers
java weblogic.WLST delete_servers.py
