#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script installs the initial setup and solution script templates into all practice folders to serve as a starting point

for folder in `find $LABHOME/$PART/practice* -print`
do
    #echo "Copying scripts to $folder..."
    #cp $TEMPLATE/* $folder
done
