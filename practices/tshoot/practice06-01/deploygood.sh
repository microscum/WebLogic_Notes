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

# copy the original version of the application from the current practice directory to the apps directory
cp contacts.war.original /u01/domains/tshoot/wlsadmin/apps/contacts.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to deploy the app (it undeploys the old version first)
java weblogic.WLST deploy_app.py

