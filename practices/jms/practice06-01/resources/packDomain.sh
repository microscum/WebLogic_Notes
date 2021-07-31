# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

DOMAIN_NAME="domain2"
DOMAIN_HOME="/u01/domains/jms/${DOMAIN_NAME}"
TEMPLATE="/tmp/${DOMAIN_NAME}.jar" 

rm -f ${TEMPLATE}

/u01/app/fmw/oracle_common/common/bin/pack.sh -managed=true -domain=${DOMAIN_HOME} -template=${TEMPLATE} -template_name="${DOMAIN_NAME} managed server template"

