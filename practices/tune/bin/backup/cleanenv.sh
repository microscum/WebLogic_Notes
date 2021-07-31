

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

##
## DO ALL LOCAL CHANGES REGARDLESS OF HOST
##

#Delete setenv.sh line from bashrc
sed -i '/setenv.sh/ d' /home/oracle/.bashrc

#Remove .part file
rm -f $HOME/.part1
rm -f $HOME/.part2
rm -f $HOME/.tune

#Recreate and populate database for course
#Script knows how to do this from either host
/practices/tune/bin/backup/BuildAuctionDatabase.sh

##
## DO ALL REMOTE CHANGES BASED ON CURRENT HOST
##

#Default remote host is host02
remote="host02"
#Perform remote operations on host02
if [ "$host" == "host02" ]; then
    remote="host01"
    #Call cleanup.sh -all to force reset.sh -skip of all practice folders (can only run on host01)
    ssh host01 "/practices/tune/bin/cleanup.sh -all"
else
    #Call cleanup.sh -all to force reset.sh -skip of all practice folders (can only run on host01)
    /practices/tune/bin/cleanup.sh -all
fi

#Delete setenv.sh line from bashrc
ssh $remote "sed -i '/setenv.sh/ d' /home/oracle/.bashrc"

#Remove .part file
ssh $remote "rm -f $HOME/.part1"
ssh $remote "rm -f $HOME/.part2"
ssh $remote "rm -f $HOME/.tune"


