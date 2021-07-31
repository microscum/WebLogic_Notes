# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

DOMAIN_NAME="domain3"
DOMAIN_HOME="/u01/domains/jms/${DOMAIN_NAME}"
TEMPLATE="/tmp/${DOMAIN_NAME}.jar"

/practices/jms/util/killAllWLS.sh
sleep 2

rm -rf $DOMAIN_HOME

/u01/app/fmw/oracle_common/common/bin/unpack.sh -domain=${DOMAIN_HOME} -template=${TEMPLATE}

