#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

for i in `ipcs -s | grep oracle | awk '{print $2}'`
do
    ipcrm -s $i
done

for i in `ipcs -q | grep oracle | awk '{print $2}'`
do
    ipcrm -q $i
done

for i in `ipcs -m | grep oracle | awk '{print $2}'`
do
    ipcrm -m $i
done




