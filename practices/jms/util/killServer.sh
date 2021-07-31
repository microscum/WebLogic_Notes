# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

wlsname=$1
wlspid=`ps -u oracle -o pid,args | grep ${wlsname} | grep -v grep | awk '{print $1}'`

if [ "" != "${wlspid}" ]; then
    kill -9 ${wlspid} > /dev/null 2>&1
    echo "Killed ${wlsname}. If node manager originally started this server, it will automatically restart it."
else
    echo "${wlsname} not found"
fi

