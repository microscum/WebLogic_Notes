#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script is the common script for this course that performs a check to ensure
#that a script is running on host02

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Perform operations only on host01
if [ "$host" != "host02" ]; then
    echo "This script must be run on host02."
    exit
fi


