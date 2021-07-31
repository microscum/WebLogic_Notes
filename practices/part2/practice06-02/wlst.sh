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
#This script makes it easy to run WLST scripts for this practice
#
# Usage: ./wlst.sh scriptname.py
#

script=$1

# $@ is for all arguments. We shift it left to get rid of the commmand script to run and pass it on
shift

echo "Script Name: $script"
echo "Args: $@"

$MW_HOME/wlserver/common/bin/wlst.sh $script $@

