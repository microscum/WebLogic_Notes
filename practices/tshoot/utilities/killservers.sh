#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

######################################################################
# This script makes sure that all weblogic processes are killed
# before proceeding. 
######################################################################

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

echo "***** Finding all java processes *****"
for procid in `ps -ef | grep weblogic.Server | egrep -v "grep|eclipse|ohs|grinder|jstatd|visual|mission" | awk '{print $2}'`
do
	echo "killing java process $procid..."
	kill -9 $procid
done





