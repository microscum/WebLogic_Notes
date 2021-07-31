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

#Reset original domain
./reset.sh

#Ensure controlled memory settings on server2
ssh host02 $bindir/createHost2SetOverrides.sh

#Start NM on host01
wlst.sh startNM.py

#Start NM on host02
ssh host02 'wlst.sh startNM.py'

#Give NMs a min to settle in
sleep 5

#Start and configure domain solution
java weblogic.WLST $PWD/solution/solution.py

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"


