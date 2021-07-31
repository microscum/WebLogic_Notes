#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script sets new custom variables for starting domains

#Set heap small so we can run a big cluster in the environment

#AdminServer uses default settings, while managed servers use custom settings
if [ "${SERVER_NAME}" != "AdminServer" ]; then
    export USER_MEM_ARGS="-Xms80m -Xmx80m -XX:MaxPermSize=256m"

    export JAVA_OPTIONS="$JAVA_OPTIONS -Djava.net.preferIPv4Stack=true"
fi


