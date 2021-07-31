#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script provides a very reliable way to check if the WLS admin server has started.
#This function is included in other scripts that start the server and need to check if it has started.
#We only need to check for the admin server because all scripting operations happen before starting managed
#servers. This provides the most efficient way of setting up and configuring practices.

#Include this script in other scripts for use with the following statement:
#source /practices/tune/bin/checkwls.sh

#Usage of function:
#After issuing command to start or shutdown the admin server, call this function:
#check_wls started
#check_wls shutdown

export SLEEPTIME=5

#Loop determining state of WLS
function check_wls {
	ACTION=$1
	while true
	do
		echo -e "***** Waiting for AdminServer to get $ACTION *****"
		sleep $SLEEPTIME
		status=`lwp-request http://host01:7001 | grep "500 Can't connect"`
		if [ "$ACTION" == "started" ] && [ -z "$status" ]; then
			break
		elif [ "$ACTION" == "shutdown" ] && [ ! -z "$status" ]; then
			break
		fi
	done
	echo -e "\nWebLogic AdminServer has $ACTION\n"
}

