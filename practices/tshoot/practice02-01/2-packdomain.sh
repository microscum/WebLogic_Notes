#!/bin/bash
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. 
# --    It is NOT supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

# set variables
DOMAIN_NAME="wlsadmin"
DOMAIN_HOME="/u01/domains/tshoot/${DOMAIN_NAME}"
TEMPLATEFILE="/tmp/${DOMAIN_NAME}.jar" 

# remove the template jar file (in case it has been created before)
rm -f ${TEMPLATEFILE}

# run the pack utility on the domain to create a managed server template (place in the /tmp directory)
/u01/app/fmw/oracle_common/common/bin/pack.sh -managed=true -domain=${DOMAIN_HOME} -template=${TEMPLATEFILE} -template_name="${DOMAIN_NAME} managed server template"

