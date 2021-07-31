#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Set OHS WL_HOME (these are scoped to the running of this script only so no need to reset)
export MW_HOME=/u01/app/ohs
export WL_HOME=$MW_HOME/wlserver

saved=$PWD

cd $OHSBIN

#Stop OHS
./stopComponent.sh ohs1 < $bindir/password | egrep -v -i "oracledms|ora_mbs"

#Stop OHS Node Manager
./stopNodeManager.sh

#Close OHS NM terminal window
wmctrl -F -c "OHS NM" 2>/dev/null

cd $saved

