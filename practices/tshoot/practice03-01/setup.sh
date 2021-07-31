#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. 
# --    It is NOT supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Create the database on host02
./initdatabase.sh

# create a directory for applications to be deployed from
mkdir /u01/domains/tshoot/wlsadmin/apps

# copy the application from the current practice directory to the apps directory
cp contacts.war /u01/domains/tshoot/wlsadmin/apps/contacts.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to create a data source
java weblogic.WLST create_data_source.py

# call WLST to deploy the app
java weblogic.WLST deploy_app.py

# call WLST to create a JMS module with a JMS server and a queue for notifications
java weblogic.WLST create_jms.py

