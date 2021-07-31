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
#within a new terminal window named server2. This script is called by our setup.sh scripts
#after the common cleanup.sh script is called to reset the domain to its original state.
bindir=/practices/part2/bin
source $bindir/checkoracle.sh

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

if [ "$host" == "host01" ]; then
    #Start server2 on host02
    ssh host02 "$bindir/startServer2.sh" &
fi

if [ "$host" == "host02" ]; then
    export DISPLAY="`grep : /home/oracle/.display`"
    cd /u01/domains/part2/wlsadmin/bin
    gnome-terminal -t "server2" -e "bash -c \"./startManagedWebLogic.sh server2 host01:7001; exec bash\""
fi


