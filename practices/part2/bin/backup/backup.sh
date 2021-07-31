#

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script manages backing up my lab development files daily
#
# TODO: Set this up as a cron job on both VMs so my daily sftp can always get the latest automatically
# This script will tar up my lab development env and give it today's date. Then once
# a day my laptop will automatically SFTP today's lab file to its
# hard drive to keep a safe copy
#
backupdir=/install/backup/saved
backupfile=$backupdir/practices_`date +%Y`_`date +%m`_`date +%d`.tar

#Get current execution host
host=`echo $HOSTNAME | sed "s/.example.com//"`

if [ ! -d "$backupdir" ]; then
    mkdir $backupdir
    mkdir $backupdir/host01
    mkdir $backupdir/host02
fi

#Copy all other files used for backup and env set up
cp -r /u01/nodemanager $backupdir/$host

#Only perform these operations on host01
if [ "$host" == "host01" ]; then
    #Delete all old copies (of practices*.tar)
    rm -f $backupdir/*.tar
    
    #PERFORM BACKUP PACKAGE (OF ALL PRACTICES FOR ALL COURSES)
    tar cvf $backupfile /practices > /dev/null 2>&1

    #Zip it all up for SFTP
    cd /install/backup
    rm -rf ftp/backup*.zip
    zip -r backup_`date +%Y`_`date +%m`_`date +%d`.zip saved/*
    mv backup*.zip ftp
    echo "Labs backed up to:" $backupfile "... " $host
fi

echo "Env and NM backed up to:" $backupdir"/"$host


