#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost02.sh

cd $bindir
sqlplus oracle/Welcome1 @../sql/deleteDatabase.sql
sqlplus oracle/Welcome1 @../sql/createDatabase.sql
cd -

