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

domaindir=/u01/domains/tshoot/wlsadmin

# check for the existence of the apps directory, create it if it does not exist
if [ ! -d "$domaindir/apps" ]; then
   echo '>>>Created the apps directory (which did not exist) under the domain.'
   mkdir $domaindir/apps
fi

# delete the old deployment plan
rm $domaindir/apps/contacts-plan.xml

# copy the new version of the application from the current practice directory to the apps directory
cp contacts.war $domaindir/apps/contacts.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to deploy the app (it undeploys the old version first)
java weblogic.WLST deploy_app.py

# call WLST to disable the WLDF system module (by targeting it to nothing)
java weblogic.WLST disable_wldf.py

