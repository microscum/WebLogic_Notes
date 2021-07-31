# .bashrc

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

export PART=jms

#Set PATH, WebLogic Env, and display file
source /practices/.internal/setcommonenv.sh

#Oddball jms bin dir set
alias bin="cd $LABHOME/\$PART/util"
alias wlsd="cd /u01/domains/\$PART/domain1"

#Course-specific aliases
alias 31="cd $LABHOME/\$PART/practice03-01"
alias 41="cd $LABHOME/\$PART/practice04-01"
alias 51="cd $LABHOME/\$PART/practice05-01"
alias 61="cd $LABHOME/\$PART/practice06-01"
alias 71="cd $LABHOME/\$PART/practice07-01"
alias 81="cd $LABHOME/\$PART/practice08-01"
alias 91="cd $LABHOME/\$PART/practice09-01"
alias 101="cd $LABHOME/\$PART/practice10-01"




