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
#that a script is being run as the root user

#Check that you are the root user
if [ -z "`id | grep root`" ]; then
    echo "This script must be run as the root user."
    exit
fi

