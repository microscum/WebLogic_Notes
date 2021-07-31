#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This is a convenience script to make it easy for students or instructors to start
#the Grinder Console and Agent processes

#Check that you are the oracle user
if [ -z "`id | grep oracle`" ]; then
    echo "This script must be run as the oracle user."
    exit
fi

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Perform operations only on host01
if [ "$host" != "host01" ]; then
    echo "This script must be run on host01."
    exit
fi

. /practices/tune/practice02-03/setenv.sh

#Open convenience terminal windows for students with Grinder env already set
gnome-terminal -t "Grinder Console" -e "bash -c \"java net.grinder.Console; exec bash;\""

#Give Console time to start up so Agent can connect
sleep 15

gnome-terminal -t "Grinder Agent" -e "bash -c \"java net.grinder.Grinder; exec bash;\""


