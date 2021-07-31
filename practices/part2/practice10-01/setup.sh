#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Set practice folders
dependent=/practices/part2/practice09-01
practice=/practices/part2/practice10-01

#Reset practice to starting state. Ensures no running servers and a clean domain.
./reset.sh

#Run shared library solution because this lab depends on that lab
cd $dependent
./solution.sh

cd $practice


