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


echo "***** Finding all Coherence cache server processes *****"
for procid in `ps -ef | grep "mycache-server.sh" | grep -v grep | grep -v "grinder" | awk '{print $2}'`
do
        echo "killing Coherence cache server process $procid..."
        kill -9 $procid
done

echo "***** Finding all java processes *****"
for procid in `ps -ef | grep java | grep -v grep | grep -v eclipse | grep -v "grinder" | awk '{print $2}'`
do
	echo "killing java process $procid..."
	kill -9 $procid
done

#Perform operations on host01
if [ "$host" == "host01" ]; then
    #Close any existing server terminal windows
    wmctrl -F -c "AdminServer"
    wmctrl -F -c "server1"
    wmctrl -F -c "server3" 2>/dev/null
    wmctrl -F -c "server5" 2>/dev/null
    wmctrl -F -c "server7" 2>/dev/null
    wmctrl -F -c "server9" 2>/dev/null
    wmctrl -F -c "Coherence Cache Server"
fi

#Perform operations on host02
if [ "$host" == "host02" ]; then
    export DISPLAY="`grep : /home/oracle/.display`"
    /usr/bin/wmctrl -F -c "server2"
    /usr/bin/wmctrl -F -c "server4" 2>/dev/null
    /usr/bin/wmctrl -F -c "server6" 2>/dev/null
    /usr/bin/wmctrl -F -c "server8" 2>/dev/null
    /usr/bin/wmctrl -F -c "server10" 2>/dev/null
    /usr/bin/wmctrl -F -c "Coherence Cache Server"
fi



