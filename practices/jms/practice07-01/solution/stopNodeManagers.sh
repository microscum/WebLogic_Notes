# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

echo "Killing node manager on host02..."
/practices/jms/util/killNM.sh
echo ""

echo "Connecting to host01 to kill node manager..."
ssh host01 "/practices/jms/util/killNM.sh"
echo ""
