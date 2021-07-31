# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

source /practices/jms/util/checkhost02.sh #Ensure script is run on the correct host

echo "Transferring template to host01..."
scp /tmp/domain4.jar host01:/tmp 
echo ""

echo "Connecting to host01 to run unpackDomain.sh..."
ssh host01 "${PWD}/unpackDomain.sh"
echo ""

echo "Connecting to host01 to run startNM.sh..."
ssh host01 "${PWD}/startNM.sh"
echo ""
