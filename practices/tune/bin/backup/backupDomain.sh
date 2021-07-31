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
# This script will be called automatically by my login. This script
# will tar up my lab development env and give it today's date. Then once
# a day my laptop will automatically SFTP today's lab file to its
# hard drive to keep a safe copy
#
backupdir=/install/backup/saved
host=`echo $HOSTNAME | sed "s/.example.com//"`

if [ ! -d "$backupdir" ]; then
    mkdir $backupdir
    mkdir $backupdir/host01
    mkdir $backupdir/host02
fi

#Delete all old copies
rm -f $backupdir/$host/wlsadmin*.tar

filename=wlsadmin_`date +%Y`_`date +%m`_`date +%d`.tar

backupfile=$backupdir/$host/$filename

#PERFORM BACKUP PACKAGE (OF ALL PRACTICES FOR ALL COURSES)
tar cvf $backupfile /u01/domains/tune/wlsadmin > /dev/null 2>&1

#echo -e "\n*******************************************************************"
echo "Domain backed up to:" $backupfile "..."
#ls -l $backupdir
#echo -e "*******************************************************************\n"


