

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#Delete setenv.sh line from bashrc
sed -i '/setenv.sh/ d' /home/oracle/.bashrc

#Remove .part file
rm -f $HOME/.part1
rm -f $HOME/.part2

