
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script updates the OES WLS SM domain's embedded LDAP with the users, groups, roles, and policy needed
# to run the secure Auction application 

import sys
import os

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

#============ Connect to server ================
def connectWLS(host):
    #WLS Must be running for this script to work
    try:
        connect('weblogic','Welcome1',host)
        print '***Connected successfully***'
    except:
        print 'Domain ' + host + ' must be running first'
        exit()

#============ Create Auditor ================
def createAuditor():
    try:
        realm=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm')
        realm.createAuditor('DefaultAuditor', 'weblogic.security.providers.audit.DefaultAuditor')
        audit=getMBean('/SecurityConfiguration/wlsadmin/Realms/myrealm/Auditors/DefaultAuditor')
        audit.setSeverity('CUSTOM')
        audit.setSuccessAuditSeverityEnabled(true)
        audit.setFailureAuditSeverityEnabled(true)
        audit.setErrorAuditSeverityEnabled(true)
    except Exception, e:
        print 'Role creation exception:'
        print e 


#============ Main Program ================
print 'Updating domain with users and groups for application'

connectWLS('t3://host01:7001')
serverConfig()
createAuditor()

disconnect('true')

print 'Completed update of domain...'
exit()
