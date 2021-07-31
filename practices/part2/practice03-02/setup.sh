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

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"
deploydir=/practices/part2/apps

#This script is run after students have manually started the domain and before using the domain

#The solution script calls reset.sh before running this script to ensure a clean starting point

#Perform deployment tasks
echo -e "\nDeploying applications for this practice\n"
java weblogic.Deployer $deployopts $deploydir/ShoppingCart.war

source ./setOPatchEnv.sh

echo -e "\nSetup is complete, continue with the next step.\n"
