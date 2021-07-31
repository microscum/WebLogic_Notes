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
deploydir=/practices/part2/apps

#Reset practice to starting state. Ensures no running servers and a clean domain.
./reset.sh

#Start AdminServer
startAdmin.sh

#Deploy practice application
java weblogic.Deployer $deployopts $deploydir/SimpleAuctionWebAppDb.war

#Start Node Manager on host01
wlst.sh startNM.py

#Start Node Manager on host02
ssh host02 "/practices/part2/bin/wlst.sh startNM.py"

#Start server1
startServer1.sh

#Start server2
startServer2.sh


