# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

SCRIPTDIR=`dirname ${BASH_SOURCE[0]}`

ORACLE_BASE=/u01/app/db11g; export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1; export ORACLE_HOME
ORACLE_SID=orcl; export ORACLE_SID
PATH=/usr/sbin:$ORACLE_HOME/bin:$PATH; export PATH

echo exit | sqlplus oracle/Welcome1 @${SCRIPTDIR}/leasing.ddl

