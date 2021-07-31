#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

practices=/practices/tune
bindir=$practices/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

echo -e "\nShutting down any java processes\n"

#Gracefully shut down domain if AdminServer is up; otherwise, skip and just kill all java procs
status=`lwp-request http://host01:7001 | grep "500 Can't connect"`
if [ -z "$status" ]; then
    wlst.sh stopDomain.py
fi

#Ensure we are starting with a clean shut down domain
$bindir/killServers.sh
ssh host02 "bash -c $bindir/killServers.sh"

