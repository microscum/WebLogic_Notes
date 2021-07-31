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

export CLASSPATH=$CLASSPATH:/practices/jms/eclipse_workspace/ProducerClients/build

java com.example.jms.GenericProducerClient Producer1 t3://host01:7011 jms.example.Factory1 jms.example.Topic1 true 5 5000

echo ""
