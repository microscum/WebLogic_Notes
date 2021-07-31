#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

practicedir=/practices/part2/practice06-01
bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost02.sh

#Start server2 on host02
cd /u01/domains/part2/SimpleAuctionDomain
mkdir -p servers/server2/security
cp /practices/part2/practice06-01/solution/boot.properties servers/server2/security

export DISPLAY="`grep : /home/oracle/.display`"
$practicedir/startServer2.sh

