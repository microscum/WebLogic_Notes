# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

echo "Updating bash_profile on host02..."
./updatePath.sh
echo ""

echo "Connecting to host01 to update bash_profile..."
ssh host01 "${PWD}/updatePath.sh"
echo ""
