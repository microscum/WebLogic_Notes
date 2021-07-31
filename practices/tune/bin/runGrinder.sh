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

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

. /practices/tune/practice02-03/setenv.sh

#Open convenience terminal windows for students with Grinder env already set
gnome-terminal -t "Grinder Console" -e "bash -c \"java -Xms50m -Xmx50m -XX:MaxPermSize=50m net.grinder.Console; exec bash;\""

#Give Console time to start up so Agent can connect
sleep 20

gnome-terminal -t "Grinder Agent" -e "bash -c \"java -Xms50m -Xmx50m -XX:MaxPermSize=50m net.grinder.Grinder; exec bash;\""


