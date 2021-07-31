#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/tune/bin
source $bindir/checkoracle.sh

#Can run from either host

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -targets cluster1"
deploydir=$PWD/resources

echo -e "\nRedeploying applications\n"

#Undeploy previous applications
java weblogic.Deployer $deployopts -undeploy -name SimpleAuctionWebAppDb1
java weblogic.Deployer $deployopts -undeploy -name SimpleAuctionWebAppDb2

#Deploy applications with specified plans
java weblogic.Deployer $deployopts -deploy -plan $deploydir/SimpleAuctionWebAppDb1-plan.xml $deploydir/SimpleAuctionWebAppDb1.war
java weblogic.Deployer $deployopts -deploy -plan $deploydir/SimpleAuctionWebAppDb2-plan.xml $deploydir/SimpleAuctionWebAppDb2.war

echo -e "\nRedeployment complete. Proceed if there are no errors.\n"



