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
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -redeploy -targets cluster1"

#Redeploy the applications with their respective deployment plans
java weblogic.Deployer $deployopts -plan $practice/resources/SimpleAuctionWebAppDb1-plan.xml -name SimpleAuctionWebAppDb1
java weblogic.Deployer $deployopts -plan $practice/resources/SimpleAuctionWebAppDb2-plan.xml -name SimpleAuctionWebAppDb2



