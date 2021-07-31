# .bashrc

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


# User specific aliases and functions

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Automatically set PART for proper course
if [ -f "$HOME/.tune" ]; then
    #echo "setting to tune"
    export PART=tune
else 
    #echo "Setting to tune because no part file exists"    
    export PART=tune
    rm -rf ~/.part1
    rm -rf ~/.part2
    touch ~/.tune
    echo ". /practices/tune/bin/setenv.sh" >> $HOME/.bashrc

    #OHS should already be installed as part of course build on host01 only:
    #Perform operations for host01
    if [ "$host" == "host01" ]; then
        cp /practices/tune/bin/mod_wl_ohs.conf /u01/app/fmw2/instances/webtier_1/config/OHS/ohs1
    fi
fi
#echo "THIS COURSE IS: $PART"
export INSTALLDIR=/install
export APP=/u01/app
export MW_HOME=$APP/fmw
export SCRIPTDIR=$HOME/bin
export JAVA_HOME=$APP/jdk
export WL_HOME=$MW_HOME/wlserver
export DBURL=localhost:1521:orcl
export ORACLE_BASE=$APP/db11g
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1
export ORACLE_SID=orcl
export LDAPHOME=$APP/ldap
export OEPEHOME=$APP/oepe
export LABHOME=/practices
export TEMPLATE=$LABHOME/$PART/template
export OHSDIR=$APP/fmw2/instances/webtier_1

#Make all PATH type variables idemopotent
if [ -z `echo $PATH | grep $JAVA_HOME` ]; then
    export PATH=$JAVA_HOME/bin:$PATH
fi
if [ -z `echo $PATH | grep ":/sbin"` ]; then
    export PATH="/sbin":$PATH
fi
if [ -z `echo $PATH | grep "db11g"` ]; then
    export PATH=$ORACLE_HOME/bin:$PATH
fi
if [ -z `echo $PATH | grep "python"` ]; then
    export PATH="/usr/lib64/python2.6/site-packages/orca/scripts/apps":$PATH
fi
if [ -z `echo $PATH | grep $OEPEHOME` ]; then
    export PATH=$OEPEHOME:$PATH
fi
#if [ -z `echo $PATH | grep "$LABHOME/$PART"` ]; then
export PATH=`echo $PATH | sed "s=$LABHOME/$PART/bin:=="`
export PATH="$LABHOME/$PART/bin":$PATH

#Automatically call setWLSEnv.sh if not set. This enforces certain paths in case students enter a command in the wrong window
#Make sure the env isn't already set first
if [ -z `echo $CLASSPATH | grep "weblogic.jar"` ]; then
    . "${WL_HOME}/server/bin/setWLSEnv.sh" >/dev/null
fi
if [ $DISPLAY ]; then
    if [ -z "`echo $DISPLAY | grep localhost`" ]; then
        echo $DISPLAY > /home/oracle/.display
    fi
fi

#Convenience aliases
alias cls=clear
alias l.='ls -d .* --color=tty'
alias ll='ls -l --color=tty'
alias ls='ls --color=tty'
alias g="gedit"
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
alias install="cd $INSTALLDIR"
alias app="cd $APP"
alias apps="cd $LABHOME/\$PART/apps"
alias ide="cd $APP/oepe"
alias fmw="cd $MW_HOME"
alias wls="cd $WL_HOME"
alias bin="cd $LABHOME/\$PART/bin"
alias ohome="cd $ORACLE_HOME"
alias dev="cd $LABHOME/\$PART/dev"
alias wlstd="cd $LABHOME/\$PART/wlst"
alias wlst="java weblogic.WLST"
alias ohs="cd $OHSDIR"

#LABS: Some labs are part1, part2, jms, troubleshoot, or tune. $PART determines which is correct for this course
alias labs="cd $LABHOME/\$PART"
alias part1="rm -rf ~/.part2; rm -rf ~/.tune; touch ~/.part1; export PART=part1"
alias part2="rm -rf ~/.part1; rm -rf ~/.tune; touch ~/.part2; export PART=part2"
alias tune="rm -rf ~/.part1; rm -rf ~/.part2; touch ~/.tune; export PART=tune"

alias domains="cd /u01/domains/\$PART"
alias wlsd="cd /u01/domains/\$PART/wlsadmin"
alias 23="cd $LABHOME/\$PART/practice02-03"
alias 31="cd $LABHOME/\$PART/practice03-01"
alias 41="cd $LABHOME/\$PART/practice04-01"
alias 42="cd $LABHOME/\$PART/practice04-02"
alias 43="cd $LABHOME/\$PART/practice04-03"
alias 44="cd $LABHOME/\$PART/practice04-04"
alias 45="cd $LABHOME/\$PART/practice04-05"
alias 46="cd $LABHOME/\$PART/practice04-06"
alias 51="cd $LABHOME/\$PART/practice05-01"
alias 52="cd $LABHOME/\$PART/practice05-02"
alias 53="cd $LABHOME/\$PART/practice05-03"
alias 61="cd $LABHOME/\$PART/practice06-01"
alias 62="cd $LABHOME/\$PART/practice06-02"
alias 71="cd $LABHOME/\$PART/practice07-01"
alias 72="cd $LABHOME/\$PART/practice07-02"
alias 73="cd $LABHOME/\$PART/practice07-03"
alias 74="cd $LABHOME/\$PART/practice07-04"
alias 75="cd $LABHOME/\$PART/practice07-05"
alias 81="cd $LABHOME/\$PART/practice08-01"
alias 82="cd $LABHOME/\$PART/practice08-02"
alias 91="cd $LABHOME/\$PART/practice09-01"
alias 92="cd $LABHOME/\$PART/practice09-02"


export PS1='$PWD>'

