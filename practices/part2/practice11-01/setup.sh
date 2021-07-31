#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Set practice folders
practice=$PWD

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"

#Reset practice to starting state. Ensures no running servers and a clean domain.
./reset.sh

#Start AdminServer
startAdmin.sh

#Deploy the starting applications
java weblogic.Deployer $deployopts $practice/resources/SimpleAuctionWebAppDb1.war
java weblogic.Deployer $deployopts $practice/resources/SimpleAuctionWebAppDb2.war

#Start server1
startServer1.sh 

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


