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

#Set OHS WL_HOME (these are scoped to the running of this script only so no need to reset)
export MW_HOME=/u01/app/ohs
export WL_HOME=$MW_HOME/wlserver

saved=$PWD

cd /u01/domains/ohs/bin

#Stop OHS
./stopComponent.sh ohs1 < $bindir/password | egrep -v -i "oracledms|ora_mbs"

#Wait for the OHS NM to start
while [ "" != "$(netstat -ln | grep 7777)" ]; do
    echo "Waiting for OHS to stop..."
    sleep 5
done
echo ">>>OHS has stopped."

#Stop OHS Node Manager
./stopNodeManager.sh

#Wait for the OHS NM to stop
while [ "" != "$(netstat -ln | grep 127.0.0.1:5556)" ]; do
    echo "Waiting for OHS Node Manager to stop..."
    sleep 5
done
echo ">>>OHS Node Manager has stopped."

#Close OHS NM terminal window
wmctrl -F -c "OHS NM" 2>/dev/null

cd $saved

