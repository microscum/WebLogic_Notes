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

#Run the initdb script
./initdb.sh

# copy the new application to the apps directory
cp supplies.war.bad /u01/domains/tshoot/wlsadmin/apps/supplies.war

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call the WLST script to create new servers in the cluster
java weblogic.WLST create_servers.py

# call the WLST script to start the new servers
java weblogic.WLST start.py

# call the WLST script to deploy the new application
java weblogic.WLST deploy_app.py

# set up a variable for the OHS instance
ORACLE_INSTANCE=/u01/domains/ohs

# copy the OHS configuration file (which is all set up) over to the right location
cp mod_wl_ohs.conf $ORACLE_INSTANCE/config/fmwconfig/components/OHS/instances/ohs1

# stop everything (in case it is running)
$bindir/stopohs.sh

# start everything (OHS)
echo ">>>Starting OHS."
$bindir/startohs.sh



