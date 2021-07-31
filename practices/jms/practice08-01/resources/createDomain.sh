# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

source /practices/jms/util/checkhost02.sh #Ensure script is run on the correct host

/practices/jms/util/killAllWLS.sh
sleep 2

DOMAIN_HOME="/u01/domains/jms/domain4"
rm -rf $DOMAIN_HOME 

source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh &> /dev/null
java weblogic.WLST createDomain.py

NM_HOME="${DOMAIN_HOME}/nodemanager"

if [ -d "$NM_HOME" ]; then
    sed -i 's/SecureListener=true/SecureListener=false/g' ${NM_HOME}/nodemanager.properties
    echo ">>>Updated nodemanager.properties"
fi
