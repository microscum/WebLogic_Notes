#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Start practice 6 servers on host02

bindir=/practices/tune/bin
source $bindir/checkoracle.sh

#This has to be hard coded because when you ssh to host02 PWD becomes /home/oracle
practicedir=/practices/tune/practice06-01
domaindir=/u01/domains/tune/wlsadmin

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

practicedir=/practices/tune/practice06-01
domaindir=/u01/domains/tune/wlsadmin

#SSH if run on host01
if [ "$host" == "host01" ]; then
    #Start servers on host02
    ssh host02 "$practicedir/startHost2Svrs.sh" &
fi

#Just run if on host02
if [ "$host" == "host02" ]; then
    export DISPLAY="`grep : /home/oracle/.display`"
    
	#Start odd servers on host02
	cd $domaindir/bin

	for i in {2..12..2}
	do
		title="server${i}"
		mkdir -p "$domaindir/servers/$title/security"
		cp "$practicedir/resources/boot.properties" "$domaindir/servers/$title/security"
		gnome-terminal -t "$title" -e "bash -c \"./startManagedWebLogic.sh $title host01:7001; exec bash\""
	done
fi









