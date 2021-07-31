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

#Tries to gracefully shutdown servers and then kills servers on both machines
#Also closes all AdminServer, server1, and server2 terminal windows
$bindir/stopDomain.sh

#Reset original domain on both hosts
echo -e "\nResetting domain on host01"
rm -rf /u01/domains/part2/wlsadmin
unzip /practices/part2/domain/wlsadmin.host01.orig.zip -d /u01/domains/part2 >/dev/null
echo -e "\nResetting domain on host02"
ssh host02 "rm -rf /u01/domains/part2/wlsadmin"
ssh host02 "unzip /practices/part2/domain/wlsadmin.host02.orig.zip -d /u01/domains/part2 >/dev/null"

echo -e "\nDomain is reset to original state\n"

exit

#Perform specific lab cleanup operations here
#If -all arg comes in this is called to cleanup the entire set of practices
#so we will execute the reset.sh script in every practice folder, passing the
#-skip option to it so that it skips calling the cleanup.sh script (this script)
if [ "$1" == "-all" ]; then
    savedir=$PWD
    cd /practices/part2
    for i in `ls -1 | grep practice | sort`
    do
        cd $i
        if [ -f "reset.sh" ]; then
            echo "Calling $i/reset.sh -skip"
            ./reset.sh -skip
        fi
        cd ..
    done
    cd $savedir
fi


