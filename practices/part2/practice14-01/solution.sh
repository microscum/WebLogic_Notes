#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Set practice folders
practice=$PWD
domaindir=/u01/domains/part2

#Reset practice to starting state. Ensures no running servers and a clean domain.
./reset.sh

#Remove original domain from each host
echo "Removing original domain."
rm -rf $domaindir/wlsadmin
ssh host02 "rm -rf $domaindir/wlsadmin"

#Place solution domain
echo "Putting solution domain in place."
unzip $practice/solution/wlsadmin.host01.solution.zip -d $domaindir
ssh host02 "unzip $practice/solution/wlsadmin.host02.solution.zip -d $domaindir"

#Start Node Manager on host01
wlst.sh startNM.py

#Start Node Manager on host02
ssh host02 "/practices/part2/bin/wlst.sh startNM.py"



