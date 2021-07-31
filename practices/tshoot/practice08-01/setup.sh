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

# copy the new version of the application from the current practice directory to the apps directory
cp contacts.war.bad /u01/domains/tshoot/wlsadmin/apps/contacts.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to redeploy the app
java weblogic.WLST redeploy_app.py

# call WLST to delete the old version of the data source (if it exists)
java weblogic.WLST delete_data_source.py

# call WLST to create the new version of the data source
java weblogic.WLST create_data_source.py
