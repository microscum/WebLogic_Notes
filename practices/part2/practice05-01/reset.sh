#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script resets practice files, the domain, and the environment to its original state

domain=/u01/domains/part2/wlsadmin
bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Handle args
#If -skip arg comes in this is called by cleanup.sh to cleanup the entire set of practices
#In this case, skip calling cleanup.sh because it is in charge already
if [ "$1" != "-skip" ]; then 
    #Reset original domain and env
    cleanup.sh
    echo -e "\nDomain, environment, and practice all reset to original state.\n"
fi

#Reset practice files

#Remove Node Manager as a service
sudo service nodemgr stop
sudo chkconfig --del nodemgr
sudo rm /etc/init.d/nodemgr
#No need to change nodemanager.properties back because the original is set in domain

#Remove all files that Node Manager uses to detect if it should restart servers
serverdir=/u01/domains/part2/wlsadmin/servers

#Takes care of files on both hosts
function clearfiles {
    server=$1
    
    #Host01    
    rm -f $serverdir/$server/data/nodemanager/$server.lck
    rm -f $serverdir/$server/data/nodemanager/$server.state
    rm -f $serverdir/$server/data/nodemanager/$server.pid

    #Host02
    ssh host02 rm -f $serverdir/$server/data/nodemanager/$server.lck
    ssh host02 rm -f $serverdir/$server/data/nodemanager/$server.state
    ssh host02 rm -f $serverdir/$server/data/nodemanager/$server.pid
}


clearfiles AdminServer
clearfiles server1
clearfiles server2




