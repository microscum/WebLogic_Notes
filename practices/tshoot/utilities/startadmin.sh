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

if [ "" == "$(netstat -ln | grep 7001)" ]; then
    echo "Starting AdminServer..."
    SAVEPATH=`pwd`
    cd $DOMAIN_HOME/bin
    ./startWebLogic.sh >AdminServer.out 2>&1 &
    cd $SAVEPATH
    while [ "" == "$(netstat -ln | grep 7001)" ]; do
        echo "Waiting for admin server to start..."
        sleep 5
    done
    echo "AdminServer started."
else
    echo "AdminServer is already running."
fi
