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

# call the setup script
./setup.sh

# set up the environment for WLST
source /u01/app/fmw/wlserver/server/bin/setWLSEnv.sh

# call WLST to create the WLDF module
java weblogic.WLST create_wldf.py
