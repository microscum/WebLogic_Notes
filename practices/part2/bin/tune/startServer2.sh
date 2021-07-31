#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script is the common script for this course that starts the server2 server on host02
#within a new terminal window named server1. This script is called by our setup.sh scripts
#after the common cleanup.sh script is called to reset the domain to its original state.

#Check that you are the oracle user
if [ -z "`id | grep oracle`" ]; then
    echo "This script must be run as the oracle user."
    exit
fi

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Perform operations only on host01
if [ "$host" == "host01" ]; then
    #Start server2 on host02
    ssh host02 "/practices/tune/bin/startServer2.sh" &
fi

if [ "$host" == "host02" ]; then
    export DISPLAY="`grep : /home/oracle/.display`"
    cd /u01/domains/tune/wlsadmin/bin
    gnome-terminal -t "server2" -e "bash -c \"./startManagedWebLogic.sh server2 host01:7001; exec bash\""
fi


