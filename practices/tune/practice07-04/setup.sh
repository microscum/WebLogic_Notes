#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script puts the wlsadmin domain into the starting state required for this practice

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Reset original domain and practice state
./reset.sh

#Start AdminServer
echo -e "\nStarting AdminServer\n"
startAdmin.sh

#Start managed servers
echo -e "\nStarting Managed Servers\n"
startServer1.sh
startServer2.sh

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


