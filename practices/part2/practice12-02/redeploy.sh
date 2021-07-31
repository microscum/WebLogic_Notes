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
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -targets cluster1"

if [ "$1" == "solution" ]; then
    deploydir=$PWD/solution
else
    deploydir=$PWD/resources
fi

#Undeploy previous applications
java weblogic.Deployer $deployopts -undeploy -name SimpleAuctionWebAppDb 2>/dev/null

#Deploy the solution application with multi data source configured JNDI name
java weblogic.Deployer $deployopts -deploy $deploydir/SimpleAuctionWebAppDb



