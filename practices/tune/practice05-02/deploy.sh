#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Can run from either host

bindir=/practices/tune/bin
source $bindir/checkoracle.sh

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -targets cluster1"
deploydir=/practices/tune/apps

#Perform deployment tasks
echo -e "\nDeploying StuckThreads application\n"
java weblogic.Deployer $deployopts -deploy $deploydir/StuckThreads.war

echo -e "\nDeployment complete. Proceed if there are no errors.\n"


