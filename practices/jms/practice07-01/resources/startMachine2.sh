# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

source /practices/jms/util/checkhost02.sh #Ensure script is run on the correct host

DOMAIN_NAME=domain3

./startNM.sh

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



