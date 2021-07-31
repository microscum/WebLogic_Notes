

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

remote="host02"
#Perform remote operations on host02
if [ "$host" == "host01" ]; then
    ssh host02 /practices/tune/bin/deleteDatabase.sh
    ssh host02 /practices/tune/bin/createDatabase.sh
    ssh host02 "/u01/app/jdk/bin/java -jar /practices/tune/apps/CreateAuctionDatabase.jar"
else
    /practices/tune/bin/deleteDatabase.sh
    /practices/tune/bin/createDatabase.sh
    /u01/app/jdk/bin/java -jar /practices/tune/apps/CreateAuctionDatabase.jar
fi



