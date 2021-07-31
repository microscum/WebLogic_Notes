#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script is the common script for this course that starts the server1 server on host01
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
if [ "$host" != "host01" ]; then
    echo "This script must be run on host01."
    exit
fi

#Start server1 on host01
cd /u01/domains/tune/wlsadmin/bin
gnome-terminal -t "server1" -e "bash -c \"./startManagedWebLogic.sh server1 host01:7001; exec bash\""





