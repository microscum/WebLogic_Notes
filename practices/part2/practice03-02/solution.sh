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

#Reset original domain
./reset.sh

#Start AdminServer
echo -e "\nStarting AdminServer\n"
startAdmin.sh

#Call setup script to deploy app and set OPatch env
source ./setup.sh

#Start managed servers
echo -e "\nStarting Managed Servers\n"
startServer1.sh
startServer2.sh

#Prepare patch
cd /practices/part2/practice03-02
mkdir PATCH_TOP
cd PATCH_TOP
unzip /install/weblogicpatch/p19234430_121300_Generic.zip -d .

#Exit in patch folder
cd 19234430    

#Open environment ready window on host02
ssh host02 ". /practices/part2/practice03-02/solution2.sh"

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


