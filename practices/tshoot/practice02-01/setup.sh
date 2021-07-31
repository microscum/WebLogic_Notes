#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. 
# --    It is NOT supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

SAVEPATH=`pwd`

#Cleanup first just in case the script must be run multiple times
echo ">>>>>Cleaning up any resources in case this script is run multiple times."
$bindir/stopohs.sh
$bindir/killallnodemanagers.sh
$bindir/killservers.sh
ssh host02 "$bindir/killservers.sh"

echo ">>>>>Creating the domain."
$SAVEPATH/1-createdomain.sh
echo ">>>>>Packing the domain."
$SAVEPATH/2-packdomain.sh
echo ">>>>>Copying the domain to host02 (and unpacking)."
$SAVEPATH/3-copydomain.sh
# Note that script 3 calls script 4 which unpacks the domain on host02
echo ">>>>>Starting Node Manager on both hosts."
$SAVEPATH/5-startnodemanagers.sh
echo ">>>>>Starting the admin server."
$SAVEPATH/../utilities/startadmin.sh
echo ">>>>>Starting OHS."
$SAVEPATH/6-ohs.sh
