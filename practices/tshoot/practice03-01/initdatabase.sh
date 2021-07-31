#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

bindir=/practices/tshoot/utilities
source $bindir/checkoracle.sh

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

if [ "$host" == "host01" ]; then
    ssh host02 ". /home/oracle/.oraenv; cd /practices/tshoot/practice03-01; ./initdatabase.sh"
fi

if [ "$host" == "host02" ]; then
# initialize the database
$ORACLE_HOME/bin/sqlplus oracle/Welcome1 << EOF
set echo off
set heading off
@init_database.sql;
exit;
EOF
fi

