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

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"
deploydir=/practices/part2/practice08-01/resources

#Reset to original state
./reset.sh

#Start AdminServer
startAdmin.sh

#Deploy practice application
java weblogic.Deployer $deployopts $deploydir/SimpleAuctionWebAppDb.war

#Start server1
startServer1.sh

echo "Set up complete. Continue with the next practice step."


   
