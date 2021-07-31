# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

echo "Starting node manager on host02..."
./startNodeManager.sh
echo ""

echo "Connecting to host01 to start node manager..."
ssh host01 "${PWD}/startNodeManager.sh"
echo ""
