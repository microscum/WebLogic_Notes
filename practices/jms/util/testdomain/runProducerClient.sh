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

if [ $# -gt 0 ]; then
    java com.example.jms.GenericProducerClient "$@"
else
    java com.example.jms.GenericProducerClient HRApp1 t3://host01:7011 jms.hr.Factory1 jms.hr.NewEmployeeQueue false 10 10000
    java com.example.jms.GenericProducerClient HRApp2 t3://host01:7011 jms.hr.Factory1 jms.hr.BenefitsTopic false 10 10000
fi

echo ""
