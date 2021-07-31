#!/bin/bash
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

# Find all processes with "grinder" but ignore the grep process
# Write results to a file for debugging
ps -u oracle -o pid,args | grep grinder | egrep -v "grep|killgrinder" > /tmp/grinderlist

# Kill each process listed in the file
rm -f /tmp/grinderfound
cat /tmp/grinderlist | while read pid prog; do
    kill -9 $pid > /dev/null 2>&1
    touch /tmp/grinderfound
done

if [ -f /tmp/grinderfound ]; then
    echo "Killed all Grinder client processes."
else
    echo "No Grinder client processes found."
fi

