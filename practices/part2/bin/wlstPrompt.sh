#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

export CLASSPATH=$CLASSPATH:$WL_HOME/server/lib/weblogic-classes.jar
. "${WL_HOME}/server/bin/setWLSEnv.sh"

java weblogic.WLST
