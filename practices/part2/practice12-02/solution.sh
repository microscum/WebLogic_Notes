#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

#Reset practice to starting state. Ensures no running servers and a clean domain.
./reset.sh

#Create database artifacts on host02
ssh host02 $bindir/startDB2.sh
ssh host02 $bindir/createDatabase2.sh

#Start AdminServer
startAdmin.sh

#Create work managers
wlst.sh createTestTable.py
wlst.sh createDataSource2.py
wlst.sh createMultiDataSource.py

#Deploy application with updated multi data source JNDI name
./redeploy.sh solution

#Start server1
startServer1.sh


