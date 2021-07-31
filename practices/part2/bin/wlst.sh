#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#
#This script makes it easy to run WLST scripts in this course
#
# Usage: ./wlst.sh scriptname.py
#
export WLSTDIR=/practices/part2/wlst

script=$1

# $@ is for all arguments. We shift it left to get rid of the commmand script to run and pass it on
shift

echo "args=$@"

. "${WL_HOME}/server/bin/setWLSEnv.sh"
java weblogic.WLST $WLSTDIR/$script $@

