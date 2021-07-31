#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

practicedir=/practices/part2/practice04-01
bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Reset practice to starting state. Even though we are working with another domain
#I call reset and let cleanup.sh work because part of its processing is to make
#sure that all WebLogic servers are shut down. That ensures a clean env for this practice.
./reset.sh

#Perform operations for host01
unzip solution/AuctionDomainHost01.zip -d /u01/domains/part2

#Perform operations for host02
ssh host02 "unzip $practicedir/solution/AuctionDomainHost02.zip -d /u01/domains/part2"
ssh host02 "sqlplus oracle/Welcome1 @$practicedir/resources/jdbc/createDatabase.sql"


