#!bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


export GRINDER_HOME=/u01/app/grinder

CLASSPATH=${GRINDER_HOME}/lib/grinder.jar:${GRINDER_HOME}/lib/picocontainer-2.13.6.jar:${GRINDER_HOME}/lib/grinder-xmlbeans-3.11.jar:$GRINDER_HOME/grinder-http-client-3.11.jar:${CLASSPATH}

export CLASSPATH

