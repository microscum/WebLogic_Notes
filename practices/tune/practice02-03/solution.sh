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

#Call setup.sh to set up original practice. Automatically calls reset.sh, which calls cleanup.sh
./setup.sh

#Perform solution tasks
echo -e "\nCopying solution files for this practice\n"
cp solution/prefsProxyOff.js /home/oracle/.mozilla/firefox/zk4vxh3s.default/prefs.js
cp solution/auction-application.py .

#Open convenience terminal windows for students with Grinder env already set
$bindir/runGrinder.sh

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


#Notes:
#Students do not need to do recording phase because we supply the file as part of the solution

