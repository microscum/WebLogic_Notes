
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Instructions for setting up cron jobs for backing up:

as oracle user:

crontab -e

Enter the following entries:
0 15 * * * /practices/part2/bin/backup/backupDomain.sh
5 15 * * * /practices/part2/bin/backup/backup.sh

This sets up the domains to backup at 3PM PT and the other overall backup script to run at 3:05PM.

At 6PM CT (4PM PT) my laptop runs a scheduled task to execute WinSCP to synchronize the backup folder with a folder on my laptop.

