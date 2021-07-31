#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

practices=/practices/tune

#Ensure this is only running on host01
if [ "$host" != "host01" ]; then
    echo "This script must only run on host01."
    exit
fi

#Ensure we are starting with a clean shut down domain
killServers.sh
ssh host02 'bash -c /practices/tune/bin/killServers.sh'

#Start NM on host01
wlst.sh startNM.py

#Start NM on host02
ssh host02 'wlst.sh startNM.py'

#Start main domain on all servers so WLST online commands can delete stuff
wlst.sh startDomain.py

