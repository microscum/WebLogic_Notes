#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Start practice 6 servers on host01

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

practicedir=$PWD
domaindir=/u01/domains/tune/wlsadmin

#Start odd servers on host01
cd $domaindir/bin

for i in {1..12..2}
do
	title="server${i}"
	mkdir -p "$domaindir/servers/$title/security"
	cp "$practicedir/resources/boot.properties" "$domaindir/servers/$title/security"
	gnome-terminal -t "$title" -e "bash -c \"./startManagedWebLogic.sh $title host01:7001; exec bash\""
done




