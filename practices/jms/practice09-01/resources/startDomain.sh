# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

/practices/jms/util/killAllWLS.sh
echo "Connecting to host02 to kill any running servers..."
ssh host02 /practices/jms/util/killAllWLS.sh

sleep 2

DOMAIN_NAME=domain1

if [ "" == "$(ps aux | grep '[w]eblogic.NodeManager')" ]; then
    echo "Starting Node Manager..."
    SAVEPATH=`pwd`
    cd /u01/domains/jms/${DOMAIN_NAME}/bin
    ./startNodeManager.sh >nm.out 2>&1 &
    cd $SAVEPATH
fi

if [ "" == "$(ps aux | grep '[w]eblogic.Server')" ]; then
    echo "Starting Admin Server..."
    SAVEPATH=`pwd`
    cd /u01/domains/jms/${DOMAIN_NAME}/bin
    ./startWebLogic.sh >AdminServer.out 2>&1 &
    cd $SAVEPATH
    while [ "" == "$(netstat -ln | grep 7001)" ]; do
        echo "Waiting for server to start..."
        sleep 10
    done
fi

source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh &> /dev/null
java weblogic.WLST startManagedServers.py


