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
source $bindir/checkhost01.sh

domaindir=/u01/domains/tshoot/wlsadmin

SAVEPATH=`pwd`

echo ">>>>>Running the setup script."
$SAVEPATH/setup.sh

echo ">>>>>Copying the JAR file to the domain's lib directory on host01."
cp $SAVEPATH/validator.jar $domaindir/lib/validator.jar

echo ">>>>>Copying the JAR file to the domain's lib directory on host02."
scp $SAVEPATH/validator.jar host02:$domaindir/lib

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to shutdown the managed servers
java weblogic.WLST shutdown.py

# call WLST to start the managed servers
java weblogic.WLST start.py
