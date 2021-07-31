# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

DOMAIN_NAME=domain4

if [ "" == "$(ps aux | grep '[w]eblogic.NodeManager')" ]; then
    echo "Starting Node Manager..."
    SAVEPATH=`pwd`
    cd /u01/domains/jms/${DOMAIN_NAME}/bin
    ./startNodeManager.sh >nm.out 2>&1 &
    while [ "" == "$(netstat -ln | grep 5556)" ]; do
        echo "Waiting for Node Manager to start..."
        sleep 10
    done
    cd $SAVEPATH
else
    echo "Node Manager is already running."
fi



