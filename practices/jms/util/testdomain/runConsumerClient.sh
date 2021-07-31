# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh &> /dev/null
echo ""

export CLASSPATH=$CLASSPATH:/practices/jms/eclipse_workspace/ConsumerClients/build

if [ $# -gt 0 ]; then
    java com.example.jms.GenericConsumerClient "$@"
else
    java com.example.jms.GenericConsumerClient HRApp1 t3://host01:7011 jms.hr.Factory1 jms.hr.NewEmployeeQueue true 60000
fi

echo ""
