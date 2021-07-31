

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script cleans up the entire environment for all the WebLogic courses
#that are deployed to the module. It enforces execution on the host01 machine
#by only the oracle user

labs=/practices
bindir=/practices/.internal
$bindir/checkoracle.sh
$bindir/checkhost01.sh

##
## DO ALL CHANGES REGARDLESS OF HOST
##

############       GENERAL CLEANUP FOR ALL COURSES

echo "Cleaning General Common..."

#Delete setenv.sh line from .bashrc, remove part file, and remove server_migration from .bash_profile
$bindir/stripbashrc.sh
ssh host02 "$bindir/stripbashrc.sh"

#Forget Firefox logins
$bindir/firefoxforget.sh
ssh host02 "$bindir/firefoxforget.sh"

#Reset all database tables (for all courses)
ssh host02 "$bindir/cleanAllDB.sh"

#Set original OHS configuration (host01 only)
cp $bindir/mod_wl_ohs.conf.orig /u01/domains/ohs/config/fmwconfig/components/OHS/instances/ohs1/mod_wl_ohs.conf

#Strip all course bin paths out of PATH
export PATH=`echo $PATH | sed "s=/practices/part1/bin:==" | sed "s=/practices/part2/bin:==" | sed "s=/practices/jms/util:==" | sed "s=/practices/tune/bin:==" | sed "s=/practices/tshoot/bin:=="`




############       ADMIN I CLEANUP

echo "Cleaning Admin I..."
#Delete all -orig folders (/u01/app/fmw-orig, /u01/app/ohs-orig, jdk, etc) host01 only
rm -rf /u01/app/fmw-orig
rm -rf /u01/app/ohs-orig
rm -rf /u01/app/jdk-orig

#Delete Grinder from /home/oracle (both hosts)
rm -rf /home/oracle/grinder*
ssh host02 "rm -rf /home/oracle/grinder*"

#Remove benefits.com from /etc/hosts for virtual host lab
$bindir/stripbashrc.sh
ssh host02 "$bindir/stripbashrc.sh"


############       ADMIN II CLEANUP

echo "Cleaning Admin II..."
#Reset all labs and domain
/practices/part2/bin/cleanup.sh -all

#Database
#ssh host02 ". /home/oracle/.oraenv; cd /practices/part2/bin; ./deleteDatabase.sh"
ssh host02 ". /home/oracle/.oraenv; cd /practices/part2/bin; ./createDatabase.sh"




############       JMS CLEANUP

echo "Cleaning JMS..."
#Remove all domains that are created in course
rm -rf /u01/domains/jms/*




############       TUNE CLEANUP

echo "Cleaning Tune..."

#Reset all labs and domain
/practices/tune/bin/cleanup.sh -all

#Remove the setUserOverrides.sh script that cleanup.sh retains
rm -f /u01/domains/tune/wlsadmin/bin/setUserOverrides.sh

#Recreate and populate database for course
#Script knows how to do this from either host
ssh host02 ". /home/oracle/.oraenv; /practices/tune/bin/backup/BuildAuctionDatabase.sh"
#TBD: Difference between Admin II createDatabase.sh (servers online?) and BuildAuctionDatabase.sh (offline)?
#Create database uses sqlplus to create tables/triggers... build uses JPA offline to populate with data




############       TSHOOT CLEANUP

echo "Cleaning Tshoot..."
#Remove all domains that are created in course
rm -rf /u01/domains/tshoot/*

#Remove managed template jar file
rm -f /tmp/wlsadmin.jar

#Remove RDA output
rm -rf /u01/app/fmw/oracle_common/rda/output
rm -rf /u01/app/fmw/oracle_common/rda/RDA_output_host01.zip

#Remove practice06-01 files
rm -f /home/oracle/server1_threads.txt

#Remove practice10-1/2 files
#TBD: mod_wl_ohs.conf file?
rm -rf /practices/tshoot/practice10-01/grinderlog
rm -rf /practices/tshoot/practice10-02/grinderlog








