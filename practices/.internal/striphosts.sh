#!/bin/bash
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script cleans up the .bashrc file and removes the part file from /practices
#This script is called by the internal cleanenv.sh script, once on host01, then again ssh host02

labs=/practices
bindir=/practices/.internal
$bindir/checkoracle.sh

##
## DO ALL CHANGES REGARDLESS OF HOST
##

#Remove benefits.com from /etc/hosts file in case it is entered in there for Admin I course
sudo sed -i "s/benefits.com//g" /etc/hosts



