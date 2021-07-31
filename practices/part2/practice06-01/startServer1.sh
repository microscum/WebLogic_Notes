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
bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Start server1 on host01
cd /u01/domains/part2/SimpleAuctionDomain/bin
gnome-terminal -t "server1" -e "bash -c \"./startManagedWebLogic.sh server1 host01:7001; exec bash\""



