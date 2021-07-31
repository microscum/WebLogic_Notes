# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------

OHS_DIR=/u01/domains/ohs
MYDIR=`pwd`

host=`echo $HOSTNAME | sed "s/.example.com//"`

if [ "$host" == "host01" ]; then
    #Copy plugin configuration
    cp mod_wl_ohs.conf $OHS_DIR/config/fmwconfig/components/OHS/instances/ohs1

    #Configure NM to use a plain connection
    /install/webtier/config/configNM.sh

    #Start OHS NM on host01
    cd $OHS_DIR/bin
    gnome-terminal -t "OHS NM" -e "bash -c \"./startNodeManager.sh; exec bash;\""
    sleep 30

    #Start OHS
    gnome-terminal -t "OHS" -e "bash -c \"./startComponent.sh ohs1 < $MYDIR/password; exec bash;\""
    sleep 30
    

    #Show OHS Status
    /u01/app/fmw/wlserver/common/bin/wlst.sh /install/webtier/config/status.py

    #Return to calling folder
    cd $MYDIR
fi



