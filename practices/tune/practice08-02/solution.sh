#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script puts the wlsadmin domain into the solution state required for this practice

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

practicedir=$PWD

#Reset original domain
./reset.sh

#Start AdminServer
echo -e "\nStarting AdminServer\n"
startAdmin.sh

#Perform solution configuration tasks (WLST, etc)
#Create work managers
echo -e "\nConfiguring domain for this practice\n"
java weblogic.WLST $practicedir/solution/createWorkManagers.py

#Perform solution deployment tasks
#Deploy applications using plans that associate work managers with each application
echo -e "\nDeploying applications for this practice\n"
./redeploy.sh

#Start managed servers
echo -e "\nStarting Managed Servers\n"
startServer1.sh
startServer2.sh

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


