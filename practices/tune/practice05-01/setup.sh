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

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"
deploydir=/practices/tune/apps

#Reset original domain and practice state
./reset.sh

#Ensure controlled memory settings on server2
ssh host02 $bindir/createHost2SetOverrides.sh

#Start wlsadmin domain with node managers
echo -e "\nStarting Domain\n"
startDomain.sh

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


