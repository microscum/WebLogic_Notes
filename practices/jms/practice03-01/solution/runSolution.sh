# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

#!/bin/sh

cd ../resources
./createDomain.sh

cd ../solution
./startDomain.sh
./configureJMS.sh

cd ../resources
./deployEJBApp.sh
