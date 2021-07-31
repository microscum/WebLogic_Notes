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

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -targets cluster1"
deploydir=$PWD/resources

#Perform deployment tasks
echo -e "\nRedeploying ShoppingCart application\n"
java weblogic.Deployer $deployopts -undeploy -name ShoppingCart
java weblogic.Deployer $deployopts -deploy $deploydir/ShoppingCart

echo -e "\nRedeployment complete. Proceed if there are no errors.\n"


