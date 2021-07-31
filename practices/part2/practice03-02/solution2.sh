#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/part2/bin
source $bindir/checkoracle.sh
source $bindir/checkhost02.sh

#Open environment ready window on host02
export DISPLAY="`grep : /home/oracle/.display`"
wmctrl -F -c "LAB WINDOW" 2>/dev/null
gnome-terminal -t "LAB WINDOW" -e "bash -c \"cd /practices/part2/practice03-02; exec bash\""


