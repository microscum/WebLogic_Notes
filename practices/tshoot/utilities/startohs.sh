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

#Set OHS WL_HOME (these are scoped to the running of this script only so no need to reset)
export MW_HOME=/u01/app/ohs
export WL_HOME=$MW_HOME/wlserver

saved=$PWD

cd /u01/domains/ohs/bin

#Start OHS Node Manager
echo ">>>Starting OHS Node Manager."
gnome-terminal -t "OHS NM" -e "bash -c \"./startNodeManager.sh; exec bash;\""

#Wait for the OHS NM to start
while [ "" == "$(netstat -ln | grep 127.0.0.1:5556)" ]; do
    echo "Waiting for OHS Node Manager to start..."
    sleep 5
done
echo ">>>OHS Node Manager has started."

#Start OHS
echo ">>>Starting OHS."
./startComponent.sh ohs1 < $bindir/password | egrep -v -i "oracledms|ora_mbs"

#Check OHS Status
echo ">>>Displaying OHS status."
$MW_HOME/oracle_common/common/bin/wlst.sh /install/webtier/config/status.py | egrep -v -i "oracledms|ora_mbs"

cd $saved



