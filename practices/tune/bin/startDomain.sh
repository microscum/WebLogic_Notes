#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Ensure we are starting with a clean shut down domain
killServers.sh
ssh host02 "bash -c $bindir/killServers.sh"

#Start NM on host01
wlst.sh startNM.py

#Start NM on host02
ssh host02 "wlst.sh startNM.py"

#Start main domain on all servers so WLST online commands can delete stuff
wlst.sh startDomain.py

