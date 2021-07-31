#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#This script creates the original domain backup for wlsadmin on each host

domain=/u01/domains/tune/wlsadmin

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`
zipfile="none"
zipfolder=/practices/tune/domain

#Perform operations for host01
if [ "$host" == "host01" ]; then
    #Kill all java processes
    killServers.sh
    ssh host02 'bash -c /practices/tune/bin/killServers.sh'

    #Delete old backups
    rm -rf $zipfolder/wlsadmin.host*

    zipfile="$zipfolder/wlsadmin.host01.orig.zip"
fi

if [ "$host" == "host02" ]; then
    zipfile="$zipfolder/wlsadmin.host02.orig.zip"
fi

#Make domain smaller and zip it up
../compactDomain.sh
cd /u01/domains/tune
zip -r $zipfile wlsadmin


#Make it a single command that is run from host01. Call the script on host02 and have it do its thing too
if [ "$host" == "host01" ]; then
	ssh host02 "cd /practices/tune/bin/backup; ./createBackupDomainZip.sh"
	echo -e "\nDomain zip backups created\n"
	ls -l $zipfolder
fi




