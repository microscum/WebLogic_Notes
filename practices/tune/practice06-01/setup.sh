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

practicedir=$PWD
domaindir=/u01/domains/tune/wlsadmin

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"
deploydir=/practices/tune/apps

#Reset original domain and practice state
./reset.sh

#Copy setUserOverrides.sh for this practice (sets memory heap small so many managed servers can run simultaneously)
cp $practicedir/resources/setUserOverrides.sh $domaindir/bin
ssh host02 "cp $practicedir/resources/setUserOverrides.sh $domaindir/bin"

#Start AdminServer
echo -e "\nStarting AdminServer\n"
startAdmin.sh

#Perform configuration tasks (WLST, etc)
echo -e "\nConfiguring domain for this practice\n"
java weblogic.WLST $practicedir/resources/createBigCluster.py

#Perform deployment tasks
echo -e "\nDeploying applications for this practice\n"
java weblogic.Deployer $deployopts $deploydir/ShoppingCart.war

#Start managed servers
echo -e "\nStarting Managed Servers\n"

#Start all servers on host01
./startHost1Svrs.sh

#Start all servers on host02
./startHost2Svrs.sh 

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


