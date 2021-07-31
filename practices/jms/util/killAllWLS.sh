# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

# Find all processes with "weblogic" but ignore the grep process
# Write results to a file
rm -f /tmp/wlslist
ps -u oracle -o pid,args | grep weblogic | grep -v grep > /tmp/wlslist

# Kill each process listed in the file
rm -f /tmp/wlsfound
cat /tmp/wlslist | while read pid prog; do
    kill -9 $pid > /dev/null 2>&1
    touch /tmp/wlsfound
done

if [ -f /tmp/wlsfound ]; then
    echo "Killed existing WLS processes. Refer to /tmp/wlslist for details"
fi

