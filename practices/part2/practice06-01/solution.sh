#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

practicedir=/practices/part2/practice06-01
bindir=/practices/part2/bin
source $bindir/checkwls.sh
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Ensure proper starting env
./reset.sh

#Copy wlst scripts here
cp solution/*.py .

#Run domain creation solution script
./wlst.sh basicWLSDomain.py

#Pack up domain
cd /u01/app/fmw/wlserver/common/bin
./pack.sh -domain=/u01/domains/part2/SimpleAuctionDomain -template=/practices/part2/practice06-01/SimpleDomainManaged.jar -template_name="My Domain Template" -managed=true

#Unpack domain on host02
ssh host02 'bash -c "cd /u01/app/fmw/wlserver/common/bin; ./unpack.sh -domain=/u01/domains/part2/SimpleAuctionDomain -template=/practices/part2/practice06-01/SimpleDomainManaged.jar -app_dir=/u01/domains/part2/SimpleAuctionDomain/apps"'

#Start servers on host01
cd /u01/domains/part2/SimpleAuctionDomain
mkdir -p servers/server1/security
cp servers/AdminServer/security/boot.properties servers/server1/security
cp servers/AdminServer/security/boot.properties /practices/part2/practice06-01/solution
$practicedir/startAdmin.sh

#Wait for AdminServer to start. Using this here means we only have to code this once.
check_wls started

#Start server1
$practicedir/startServer1.sh

#Start server2
ssh host02 "/practices/part2/practice06-01/solution2.sh" &

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"



