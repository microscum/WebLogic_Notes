#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Check that you are the oracle user
if [ -z "`id | grep oracle`" ]; then
    echo "This script must be run as the oracle user."
    exit
fi

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Perform operations only on host01
if [ "$host" != "host01" ]; then
    echo "This script must be run on host01."
    exit
fi

#Tries to gracefully shutdown servers and then kills servers on both machines
#Also closes all AdminServer, server1, and server2 terminal windows
stopDomain.sh

#Reset original domain on both hosts
echo -e "\nResetting domain on host01"
rm -rf /u01/domains/tune/wlsadmin
unzip /practices/tune/domain/wlsadmin.host01.orig.zip -d /u01/domains/tune >/dev/null
echo -e "\nResetting domain on host02"
ssh host02 "rm -rf /u01/domains/tune/wlsadmin"
ssh host02 "unzip /practices/tune/domain/wlsadmin.host02.orig.zip -d /u01/domains/tune >/dev/null"

echo -e "\nDomain is reset to original state\n"

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


