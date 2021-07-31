#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script is the common script for this course that starts the AdminServer on host01
#within a new terminal window named AdminServer. This script is called by our setup.sh scripts
#after the common cleanup.sh script is called to reset the domain to its original state.
#The setup script calls this script, the AdminServer starts, we wait for the server to successfully
#start, and execution is returned to the setup.sh or solution.sh script to do whatever configuration
#is needed prior to starting any managed servers. Managed servers that start after configuration will
#get the updated configuration from the AdminServer during startup. 

bindir=/practices/part2/bin

source $bindir/checkwls.sh
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Start AdminServer on host01
cd /u01/domains/part2/SimpleAuctionDomain
gnome-terminal -t "AdminServer" -e "bash -c \"./startWebLogic.sh; exec bash;\""

#Wait for AdminServer to start. Using this here means we only have to code this once.
check_wls started


