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
./packDomain.sh

cd ../solution
./startMachine1.sh
./startMachine2.sh
./createDynCluster.sh
./configureJMS.sh
./startServers.sh

cd ../resources
./deployEJBApp.sh
