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

# set variables
DOMAIN_NAME="wlsadmin"
TEMPLATEFILE="/tmp/${DOMAIN_NAME}.jar" 

#Delete template file in case run multiple times
ssh host02 "rm -f $TEMPLATEFILE"

echo "Copying managed server template to host02 by using secure copy"
scp $TEMPLATEFILE host02:/tmp
echo "Running the unpack domain script on host02 by using ssh"
ssh host02 "${PWD}/4-unpackdomain.sh"
