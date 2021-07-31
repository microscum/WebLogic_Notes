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

#Set deployer command line options
deployopts="-adminurl host01:7001 -username weblogic -password Welcome1 -deploy -targets cluster1"
deploydir=/practices/tune/apps

practicedir=$PWD

#Reset original domain and practice state
./reset.sh

#Start AdminServer
echo -e "\nStarting AdminServer\n"
startAdmin.sh

#Perform dependency scripts
java weblogic.WLST $practicedir/../practice07-01/solution/configureConnPool01.py
java weblogic.WLST $practicedir/../practice07-02/solution/configureConnPool02.py

#Perform deployment tasks
echo -e "\nDeploying applications for this practice\n"
java weblogic.Deployer $deployopts $deploydir/SimpleAuctionDbSLSB_EAR.ear

#Start managed servers
echo -e "\nStarting Managed Servers\n"
startServer1.sh
startServer2.sh

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"

#Start NM on host01
wlst.sh startNM.py

#Start NM on host02
ssh host02 'wlst.sh startNM.py'


