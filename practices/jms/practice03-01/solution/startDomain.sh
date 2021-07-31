# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

if [ "" == "$(ps aux | grep '[w]eblogic.NodeManager')" ]; then
    echo "Starting Node Manager..."
    SAVEPATH=`pwd`
    cd /u01/domains/jms/domain1/bin
    ./startNodeManager.sh >nm.out 2>&1 &
    cd $SAVEPATH
fi

if [ "" == "$(ps aux | grep '[w]eblogic.Server')" ]; then
    echo "Starting Admin Server..."
    SAVEPATH=`pwd`
    cd /u01/domains/jms/domain1/bin
    ./startWebLogic.sh >AdminServer.out 2>&1 &
    cd $SAVEPATH
    while [ "" == "$(netstat -ln | grep 7001)" ]; do
        echo "Waiting for server to start..."
        sleep 10
    done
fi

source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh &> /dev/null
java weblogic.WLST startManagedServers.py


