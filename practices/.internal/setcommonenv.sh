# .bashrc

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

labs=/practices
internal=/practices/.internal
bindir="bin"

alias int="cd $internal"

#Determine which host this script is running on
host=`echo $HOSTNAME | sed "s/.example.com//"`

#Useful message to let you know which course is set in environment
#echo "Setting common env for $PART: $host"

#Automatically configure for first run
if [ ! -f "$labs/.$PART" ]; then
    echo "Setting to $PART because no part file exists"    
    
    #Perform operations for host01
    if [ "$host" == "host01" ]; then
        echo "Setting up initial environment for host01"

        $internal/cleanenv.sh #Resets module to no course and cleans up artifacts

        #Set module for $PART env on both machines
        touch $labs/.$PART
        echo ". $internal/$PART.sh" >> $HOME/.bashrc
        ssh host02 "echo '. $internal/$PART.sh' >> $HOME/.bashrc"

        #Set OHS up based on the course env
        if [ "$PART" == "part2" ]; then
            #OHS should already be installed as part of Admin II course build on host01 only
            cp /practices/part2/bin/mod_wl_ohs.conf /u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1
        fi
        if [ "$PART" == "tune" ]; then
            #OHS should already be installed as part of course build on host01 only
            cp /practices/tune/bin/mod_wl_ohs.conf /u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1
        fi
    fi
fi

#JMS course uses different bin folder
if [ "$PART" == "jms" ]; then
    bindir="util"
fi

#Common environment variables for all courses
export INSTALLDIR=/install
export APP=/u01/app
export MW_HOME=$APP/fmw
export JAVA_HOME=$APP/jdk
export WL_HOME=$MW_HOME/wlserver
export DBURL=host02.example.com:1521:orcl
export ORACLE_BASE=$APP/db11g
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/dbhome_1
export ORACLE_SID=orcl
export LDAPHOME=$APP/ldap
export OEPEHOME=$APP/oepe
export LABHOME=/practices
export OHSDIR=/u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1
export OHSBIN=/u01/domains/ohs/bin

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

#Strip all course bin paths out of PATH
export PATH=`echo $PATH | sed "s=/practices/part1/bin:==" | sed "s=/practices/part2/bin:==" | sed "s=/practices/jms/util:==" | sed "s=/practices/tune/bin:==" | sed "s=/practices/tshoot/bin:=="`

#Set only this course's bin in PATH
export PATH="$LABHOME/$PART/$bindir":$PATH

#Automatically call setWLSEnv.sh if not set. This enforces certain paths in case students enter a command in the wrong window
#Make sure the env isn't already set first
if [ -z `echo $CLASSPATH | grep "weblogic.jar"` ]; then
    . "${WL_HOME}/server/bin/setWLSEnv.sh" >/dev/null
fi

#Set the display into a file so we can use it when remotely opening windows on host02
if [ $DISPLAY ]; then
    if [ -z "`echo $DISPLAY | grep localhost`" ]; then
        echo $DISPLAY > /home/oracle/.display
    fi
fi

#Common Convenience Aliases for all courses (some won't work for certain courses but not a big deal)
alias cls=clear
alias l.='ls -d .* --color=tty'
alias ll='ls -l --color=tty'
alias ls='ls --color=tty'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
alias g="gedit"
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
alias ohsbin="cd $OHSBIN"

#LABS: $PART determines which course
alias labs="cd $LABHOME/\$PART"

alias domains="cd /u01/domains/\$PART"
alias wlsd="cd /u01/domains/\$PART/wlsadmin"

export PS1='$PWD>'




