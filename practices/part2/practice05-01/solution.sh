#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

domain=/u01/domains/part2/wlsadmin
bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Reset practice to starting state
./reset.sh

#Perform operations for host01
#Configure nodemgr as a service and start NM
sudo cp resources/nodemgr /etc/init.d
sudo chmod 755 /etc/init.d/nodemgr
sudo chkconfig --add nodemgr
sed -i "s/CrashRecoveryEnabled=false/CrashRecoveryEnabled=true/" $domain/nodemanager/nodemanager.properties    
sudo service nodemgr start

#Start NM on host02
ssh host02 "/practices/part2/bin/wlst.sh startNM.py"
sleep 15

#Start domain using NM
/practices/part2/bin/wlst.sh startDomain.py

#Students now perform lab instructions to kill host01 and restart it

echo -e "\nWait for all servers to fully start, then continue with the next step.\n"

