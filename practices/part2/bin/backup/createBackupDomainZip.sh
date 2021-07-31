#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#This script creates backup 

domain=/u01/domains/part2/wlsadmin

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`
zipfile="none"
zipfolder=/practices/part2/domain

#Perform operations for host01
if [ "$host" == "host01" ]; then
    #Kill all java processes
    killServers.sh
    ssh host02 'bash -c /practices/part2/bin/killServers.sh'

    #Delete old backups
    rm -rf $zipfolder/*

    zipfile="$zipfolder/wlsadmin.host01.orig.zip"
fi

if [ "$host" == "host02" ]; then
    zipfile="$zipfolder/wlsadmin.host02.orig.zip"
fi

#Make domain smaller and zip it up
./compactDomain.sh
cd /u01/domains/part2
zip -r $zipfile wlsadmin

