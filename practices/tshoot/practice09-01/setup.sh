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

# set variables
SAVEPATH=`pwd`

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to make a server2 config change
java weblogic.WLST update.py

# call WLST to shutdown server2
java weblogic.WLST shutdown.py

# copy a file over to host02
scp files/file.txt host02:/u01/domains/tshoot/wlsadmin/nodemanager/nodemanager.domains

echo ">>>>>Killing Node Manager on host02 by using ssh..."
ssh host02 "${SAVEPATH}/../utilities/killnodemanager.sh"

echo ">>>>>Starting Node Manager on host02 by using ssh..."
ssh host02 "${SAVEPATH}/../utilities/startnodemanager.sh"
