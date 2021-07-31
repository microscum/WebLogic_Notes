#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Script to reset environment:
#Kills all WebLogic/NM servers both machines
#Unzips original domain to both machines
#If called with -all then calls all tune practice reset.sh scripts with -skip arg to not call this script
#Cleans any random/global files that need cleaning

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

domainparent=/u01/domains/tune
domainbin=$domainparent/wlsadmin/bin
archivedir=/practices/tune/domain

# CHECK EXISTING USER FILE
#Special setUserOverrides.sh file handling here. If a student already has a setUserOverrides.sh file in place
#it would be best to renew the domain and then place their existing file back into the domain for convenience.
#If they didn't have one, then copy the practice's default
defaultUserFile=/practices/practice04-01/resources/setUserOverrides.sh
userFileExists=false

#Check if student has a file already
if [ -f "$domainbin/setUserOverrides.sh" ]; then
    echo "Copying existing setUserOverrides.sh script for reuse in fresh domain..."
    cp $domainbin/setUserOverrides.sh /tmp
    userFileExists=true
fi


#### STOP DOMAIN
#Tries to gracefully shutdown servers and then kills servers on both machines
#Also closes all AdminServer, server1, and server2 terminal windows
$bindir/stopDomain.sh


#### REFRESH ORIGINAL DOMAIN
#Reset original domain on both hosts
echo -e "\nResetting domain on host01"
rm -rf $domainparent/wlsadmin
unzip $archivedir/wlsadmin.host01.orig.zip -d $domainparent >/dev/null
echo -e "\nResetting domain on host02"
ssh host02 "rm -rf $domainparent/wlsadmin"
ssh host02 "unzip $archivedir/wlsadmin.host02.orig.zip -d $domainparent >/dev/null"


#### SET CORRECT USER FILE
#Put setUserOverrides.sh file in place if it existed previously or this is a compatible practice
if [ "$1" == "-userfile" ]; then
    #Only copy default file if the practice is right
    cp $defaultUserFile $domainbin
elif [ "$1" == "-nouserfile" ]; then
    #Force no userfile if requested
    rm -f $domainbin/setUserOverrides.sh
elif [ $userFileExists == true ]; then
    #Copy student's existing file to domain. Use mv to automatically remove file from /tmp
    mv /tmp/setUserOverrides.sh $domainbin
fi

#Status message
echo -e "\nDomain is reset to original state\n"


# COURSE CLEANUP/RESET WORK IF -all SET
#Perform specific lab cleanup operations here
#If -all arg comes in this is called to cleanup the entire set of practices
#so we will execute the reset.sh script in every practice folder, passing the
#-skip option to it so that it skips calling the cleanup.sh script (this script)
if [ "$1" == "-all" ]; then
    savedir=$PWD
    cd /practices/tune
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

    #Perform global deletes for labs that don't require a folder of their own
    #Practice 3-2
    rm -rf /tmp/*.txt

    #Practice 3-3
    rm -rf /tmp/*.log.*
fi


