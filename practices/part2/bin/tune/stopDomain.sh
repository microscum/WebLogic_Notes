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

echo -e "\nShutting down any java processes\n"

#Gracefully shut down domain if AdminServer is up; otherwise, skip and just kill all java procs
status=`lwp-request http://host01:7001 | grep "500 Can't connect"`
if [ -z "$status" ]; then
    wlst.sh stopDomain.py
fi

#Ensure we are starting with a clean shut down domain
killServers.sh
ssh host02 'bash -c /practices/tune/bin/killServers.sh'

