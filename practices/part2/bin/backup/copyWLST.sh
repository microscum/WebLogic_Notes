#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


cd /practices/part2
for i in `find . -name "*.py" -print | egrep -v "wls11glabs|list-auction|WLSTProject|resources"`
do
    cp $i /practices/part2/dev/WLSTProject/wlst
done
cd -
