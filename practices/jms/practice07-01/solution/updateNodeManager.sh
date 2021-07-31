# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

NMFILE=/u01/domains/jms/domain3/nodemanager/nodemanager.properties

if grep -q eth0 $NMFILE ; then
    echo "File already updated."
else
    cp -f $NMFILE $NMFILE.bak
    echo "eth0=192.0.2.20-192.0.2.30,NetMask=255.255.255.0" >> $NMFILE
    echo "File updated."
fi

