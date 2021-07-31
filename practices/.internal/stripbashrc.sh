

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script cleans up the .bashrc file and removes the part file from /practices
#This script is called by the internal cleanenv.sh script, once on host01, then again ssh host02

labs=/practices
bindir=/practices/.internal
$bindir/checkoracle.sh

##
## DO ALL CHANGES REGARDLESS OF HOST
##

#Delete setenv.sh line from .bashrc
sed -i "/setenv.sh/ d" /home/oracle/.bashrc
sed -i "/part1.sh/ d" /home/oracle/.bashrc
sed -i "/part2.sh/ d" /home/oracle/.bashrc
sed -i "/jms.sh/ d" /home/oracle/.bashrc
sed -i "/tune.sh/ d" /home/oracle/.bashrc
sed -i "/tshoot.sh/ d" /home/oracle/.bashrc

#Remove server_migration path from .bash_profile
sed -i "s=:/u01/domains/jms/domain3/bin/server_migration==g" /home/oracle/.bash_profile

#Remove all .part files $labs is shared across both machines so no need to ssh
rm -f $labs/.part1 $labs/.part2 $labs/.jms $labs/.tune $labs/.tshoot



