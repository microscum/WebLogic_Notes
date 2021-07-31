# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

#!/bin/sh

source /practices/jms/util/checkhost02.sh #Ensure script is run on the correct host

cd ../resources
./createDomain.sh
./packDomain.sh
./startMachine2.sh
./startMachine1.sh

cd ../solution
./configureJMS.sh
./updatePaths.sh
./stopNodeManagers.sh
./updateNodeManagers.sh
./startNodeManagers.sh
./runDBScript.sh
./updateServers.sh
./configureServerMigration.sh
#./startServers.sh
