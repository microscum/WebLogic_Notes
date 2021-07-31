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

echo ">>>Copying completed OHS configuration file to the OHS instance."
cp mod_wl_ohs.conf /u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1

#Start OHS using the utility script
$bindir/startohs.sh




