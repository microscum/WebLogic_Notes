

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script cleans up the entire environment for all the WebLogic courses
#that are deployed to the module. It enforces execution on the host01 machine
#by only the oracle user

labs=/practices
bindir=/practices/.internal
$bindir/checkoracle.sh
$bindir/checkhost02.sh

ORACLE_BASE=/u01/app/db11g; export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1; export ORACLE_HOME
ORACLE_SID=orcl; export ORACLE_SID
ORACLE_TERM=xterm; export ORACLE_TERM
PATH=/usr/sbin:$PATH; export PATH
PATH=$ORACLE_HOME/bin:$PATH; export PATH

LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib; export LD_LIBRARY_PATH

#Reset all database tables (for all courses) (drop sequences first)
sqlplus oracle/Welcome1 <<!
DROP SEQUENCE SEQ_CONTACT;
drop table TLOG_CLUSTER2SERVER_1_WLSTORE;
drop table TLOG_CLUSTER2SERVER_2_WLSTORE;
drop table TLOG_CLUSTER2SERVER_3_WLSTORE;
drop table TLOG_CLUSTER2SERVER_4_WLSTORE;
drop table TLOG_SERVER1_WLSTORE;
drop table TLOG_SERVER2_WLSTORE;
drop table TLOG_SERVER3_WLSTORE;
drop table DYNCLUSTER1_1_WLSTORE;
drop table DYNCLUSTER1_2_WLSTORE;
drop table CONTACTS;
drop table CATALOG;
drop table IMAGE;
drop table BID;
drop table AUCTION;
drop table TEST_BATCH_UPD;
drop table Store1_WLStore;
drop table Store1WLStore;
drop table Store2WLStore;
drop table Store3WLStore;
drop table ACTIVE;
exit;
!


