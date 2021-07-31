# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

rm -f $PWD/managedserver*

ORACLE_COMMON=/u01/app/fmw/oracle_common/common/bin
#First pack on host01 to ensure we have the freshest and latest copy of the actual domain
ssh host01 "$ORACLE_COMMON/pack.sh -domain=/u01/domains/part1/wlsadmin -template=/practices/part1/practice04-02/managedserver.jar -template_name=wlsadmin_managed -managed=true"

sleep 10

$ORACLE_COMMON/unpack.sh -domain=/u01/domains/part1/wlsadmin -template=managedserver.jar


