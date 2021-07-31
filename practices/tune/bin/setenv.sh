# .bashrc

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

export PART=tune

# User specific aliases and functions
labs=/practices
bindir=$labs/$PART/bin
source $bindir/checkoracle.sh

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Automatically set PART for proper course
if [ ! -f "$labs/.tune" ]; then
    #echo "Setting to tune because no part file exists"

    #Strip all course bin paths out of PATH
    export PATH=`echo $PATH | sed "s=/practices/part1/bin:==" | sed "s=/practices/part2/bin:==" | sed "s=/practices/jms/util:==" | sed "s=/practices/tune/bin:==" | sed "s=/practices/tshoot/bin:==" | sed "s=:/u01/domains/jms/domain3/bin/server_migration==g"`    

    #Delete setenv.sh line from .bashrc
    sed -i '/setenv.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/setenv.sh/ d' /home/oracle/.bashrc"
    sed -i '/part1.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/part1.sh/ d' /home/oracle/.bashrc"
    sed -i '/part2.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/part2.sh/ d' /home/oracle/.bashrc"
    sed -i '/jms.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/jms.sh/ d' /home/oracle/.bashrc"
    sed -i '/tune.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/tune.sh/ d' /home/oracle/.bashrc"
    sed -i '/tshoot.sh/ d' /home/oracle/.bashrc
    ssh host02 "sed -i '/tshoot.sh/ d' /home/oracle/.bashrc"

    #Remove all .part files $labs is shared across both machines so no need to ssh
    rm -f $labs/.part1 $labs/.part2 $labs/.jms $labs/.tune $labs/.tshoot    

    touch $labs/.tune
    echo ". /practices/tune/bin/setenv.sh" >> $HOME/.bashrc
    ssh host02 "echo '. $bindir/setenv.sh' >> $HOME/.bashrc"

    #Perform operations for host01
    if [ "$host" == "host01" ]; then
        #Reset domain to original state on both machines
        $bindir/cleanup.sh

        #OHS should already be installed as part of course build on host01 only:
        cp $bindir/mod_wl_ohs.conf /u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1

        #Ensure Firefox doesn't remember passwords the first time this is run (only needed on host01)
        /practices/.internal/firefoxforget.sh
    fi
fi
#echo "THIS COURSE IS: $PART"
export INSTALLDIR=/install
export APP=/u01/app
export MW_HOME=$APP/fmw
export SCRIPTDIR=$HOME/bin
export JAVA_HOME=$APP/jdk
export WL_HOME=$MW_HOME/wlserver
export DBURL=host02.example.com:1521:orcl
export ORACLE_BASE=$APP/db11g
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1
export ORACLE_SID=orcl
export LDAPHOME=$APP/ldap
export OEPEHOME=$APP/oepe
export LABHOME=$labs
export TEMPLATE=$LABHOME/$PART/template
export OHSBIN=/u01/domains/ohs/bin
export OHSDIR=/u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1

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
export PATH=`echo $PATH | sed "s=$bindir:=="`
export PATH="$bindir":$PATH

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
alias bin="cd $bindir"
alias ohome="cd $ORACLE_HOME"
alias dev="cd $LABHOME/\$PART/dev"
alias wlstd="cd $LABHOME/\$PART/wlst"
alias wlst="java weblogic.WLST"
alias ohs="cd $OHSDIR"
alias ohsbin="cd $OHSBIN"

#LABS: Some labs are part1, part2, jms, troubleshoot, or tune. $PART determines which is correct for this course
alias labs="cd $LABHOME/\$PART"

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
alias 81="cd $LABHOME/\$PART/practice08-01"
alias 82="cd $LABHOME/\$PART/practice08-02"
alias 91="cd $LABHOME/\$PART/practice09-01"
alias 92="cd $LABHOME/\$PART/practice09-02"


export PS1='$PWD>'

