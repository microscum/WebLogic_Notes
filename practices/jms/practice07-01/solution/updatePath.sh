# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

#!/bin/sh

if grep -q server_migration ~/.bash_profile ; then
    echo "File already updated."
else
    cp -f ~/.bash_profile ~/.bash_profile.bak
    echo -e "export PATH=\$PATH:/u01/domains/jms/domain3/bin/server_migration" >> ~/.bash_profile
    echo "File updated."
fi

