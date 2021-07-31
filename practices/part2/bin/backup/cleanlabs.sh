#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#This script cleans up the WLS 12c Admin 2 lab environment to bring it to the starting point
#and to minimize the total size of the practices folder

echo "This script is obsolete. Use /practices/.internal/cleanenv.sh instead."
exit

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

practices=/practices/part2

#Ensure this is only running on host01
if [ "$host" != "host01" ]; then
    echo "This script must only run on host01."
    exit
fi

#Ensure we are starting with a clean shut down domain
killServers.sh
ssh host02 'bash -c /practices/part2/bin/killServers.sh'

#Remove all unneeded files from practices
rm -f /u01/domains/part2/wlsadmin/servers/AdminServer/logs/DefaultAuditRecorder.log
rm -f /u01/domains/part2/wlsadmin/servers/server1/logs/DefaultAuditRecorder.log
rm -rf $practices/practice03-01/PATCH_TOP
rm -rf $practices/practice06-01/*.py
rm -rf $practices/practice06-01/SimpleDomainManaged.jar
rm -rf /u01/domains/part2/SimpleAuctionDomain
ssh host02 'bash -c "rm -rf /u01/domains/part2/SimpleAuctionDomain"'
rm -rf $practices/practice06-02/*.py
rm -rf $practices/practice07-01/*.jks
rm -rf $practices/practice07-01/*.pem
rm -rf $practices/practice08-01/plan
rm -rf $practices/practice10-01/AuctionWebApp
rm -rf $practices/practice11-01/logs-db*
rm -rf $practices/practice14-01/*.DAT

#Start NM on host01
wlst.sh startNM.py

#Start NM on host02
ssh host02 'wlst.sh startNM.py'

#Start main domain on all servers so WLST online commands can delete stuff
wlst.sh startDomain.py

#Run all WLST delete commands to ensure domain is in initial state
wlst.sh deleteAuditProvider.py
wlst.sh deleteDataSource2.py
wlst.sh deleteMultiDataSource.py
wlst.sh deleteNetworkChannel.py
wlst.sh deleteReplicationChannel.py
wlst.sh deleteSecurityArtifacts.py
wlst.sh removeTestTable.py

#Clean up the database
deleteDatabase.sh
createDatabase.sh

#Ensure the initial domain dpeloyment is correct
wlst.sh undeployall.py d
wlst.sh deploy.py d solution/ShoppingCart.war

#Shut down domain and NMs on both machines
killServers.sh
ssh host02 'bash -c /practices/part2/bin/killServers.sh'

#Remove bloat from the main domain
compactDomain.sh

exit
#This stuff needs to run as root
#Remove Node Manager as a service
service nodemgr stop
chkconfig --del nodemgr
rm /etc/init.d/nodemgr
sed -i "s/CrashRecoveryEnabled=true/CrashRecoveryEnabled=false/" /u01/nodemanager/nodemanager.properties
