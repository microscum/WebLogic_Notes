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

#Works on either host

wlspid=`ps -u oracle -o pid,args | grep weblogic.NodeManager | grep -v grep | awk '{print $1}'`

if [ "" != "${wlspid}" ]; then
    kill -9 ${wlspid} > /dev/null 2>&1
    echo ">>>Killed Node Manager"
else
    echo ">>>Node Manager was not running"
fi

