# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

echo "Updating nodemanager.properties on host02..."
./updateNodeManager.sh
echo ""

echo "Connecting to host01 to update nodemanager.properties..."
ssh host01 "${PWD}/updateNodeManager.sh"
echo ""
