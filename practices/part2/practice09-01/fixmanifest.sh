#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script ensures that there are no ^M characters at the end of any manifest files in this practice

fixdir=/practices/part2/practice09-01

find $fixdir -name "MANIFEST.MF" | xargs sed -i "s/$//"

