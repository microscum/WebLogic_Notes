#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#This script is used to reduce the enormous size of the course domain. the log files and
#internal deployment files greatly increase the size of the domain and can safely be removed.
#This makes it easier to create VM images, and also for students to copy and replace domains. Not to mention
#that it makes backing up the devleopment environment easier.

domain=/u01/domains/part2/wlsadmin

#Remove unneeded domain files from wlsadmin domain
rm -f $domain/servers/AdminServer/data/store/diagnostics/WLS_DIAGNOSTICS000000.DAT
rm -f $domain/servers/server1/data/store/diagnostics/WLS_DIAGNOSTICS000000.DAT
rm -f $domain/servers/server2/data/store/diagnostics/WLS_DIAGNOSTICS000000.DAT
#rm -f $domain/servers/AdminServer/data/ldap/ldapfiles/changelog.data
rm -rf $domain/servers/AdminServer/tmp/.appmergegen_*
rm -rf $domain/servers/AdminServer/tmp/_WL_TEMP_APP_DOWNLOADS/*
rm -rf $domain/servers/AdminServer/logs/*.log*
rm -rf $domain/servers/server1/logs/*.log*
rm -rf $domain/servers/server2/logs/*.log*

