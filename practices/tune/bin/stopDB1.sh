#ORACLE_HOME is already set aas part of the environment: /u01/app/db11g/product/11.2.0/dbhome_1

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost02.sh

export ORACLE_SID=orcl

$ORACLE_HOME/bin/lsnrctl stop LISTENER_ORCL

$ORACLE_HOME/bin/sqlplus "/ as sysdba" <<!
shutdown immediate
exit
!

