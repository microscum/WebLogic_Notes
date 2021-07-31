# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

echo "Transferring template to host02..."
scp /tmp/domain2.jar host02:/tmp 
echo ""

echo "Connecting to host02 to run unpackDomain.sh..."
ssh host02 "${PWD}/../resources/unpackDomain.sh"
echo ""

echo "Connecting to host02 to run startNM.sh..."
ssh host02 "${PWD}/startNM.sh"
echo ""
