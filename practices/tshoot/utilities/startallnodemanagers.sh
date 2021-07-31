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

# set variables
DOMAIN_NAME=wlsadmin
DOMAIN_HOME="/u01/domains/tshoot/${DOMAIN_NAME}"
SAVEPATH=`pwd`

echo "Starting Node Manager on host01..."
$SAVEPATH/startnodemanager.sh
echo "Starting Node Manager on host02 by using ssh..."
ssh host02 "${SAVEPATH}/startnodemanager.sh"
