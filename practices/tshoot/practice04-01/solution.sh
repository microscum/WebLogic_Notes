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
   echo '>>>Created the apps directory under the domain.'
   mkdir $domaindir/apps
fi

# copy the app and deployment plan from the solution directory to the apps directory
echo '>>>Copying the new contacts application and its deployment plan to the apps directory.'
cp solution/contacts.war $domaindir/apps/contacts.war
cp solution/contacts-plan.xml $domaindir/apps/contacts-plan.xml

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# create the system-scoped diagnostic module (in case it does not exist, which it should)
java weblogic.WLST solution/create_diagnostic_module.py

# enable instrumentation
java weblogic.WLST solution/enable_instrumentation.py

# call WLST to deploy the application
java weblogic.WLST solution/deploy_app.py
