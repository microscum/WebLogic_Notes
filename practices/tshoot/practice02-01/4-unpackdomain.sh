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
source $bindir/checkhost02.sh

# set variables
DOMAIN_NAME="wlsadmin"
DOMAIN_HOME="/u01/domains/tshoot/${DOMAIN_NAME}"
TEMPLATE="/tmp/${DOMAIN_NAME}.jar"

#Delete domain just in case run multiple times
rm -rf $DOMAIN_HOME

# run the unpack utility against the managed server template to create the domain
/u01/app/fmw/oracle_common/common/bin/unpack.sh -domain=${DOMAIN_HOME} -template=${TEMPLATE}

