#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


host=`echo $HOSTNAME | sed "s/.example.com//"`

echo "Host=$host"

if [ "$host" != "host02" ]; then
    echo "This script can only run on host02"
    exit 1
fi

cd /practices/tune/bin
sqlplus oracle/Welcome1 @../sql/createDatabase.sql
cd -

