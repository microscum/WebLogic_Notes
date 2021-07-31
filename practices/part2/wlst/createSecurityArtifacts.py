
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
import weblogic.security.service.URLResource

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

#============ Create Policy ================
def createPolicy():
    authz=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/Authorizers/XACMLAuthorizer')

    #URLResource(application, context_path, pattern, httpMethod, transport)
    r=weblogic.security.service.URLResource('SimpleAuctionWebAppDbSec','/SimpleAuctionWebAppDbSec','/createAuction.jsp',None,None)
    resourceID=r.toString()
    expression='Rol(creator)'
  
    print 'creating policy: ' + resourceID + ', ' + expression
    try:
        authz.createPolicy(resourceID, expression)
        print ' '
    except Exception, e:
        print 'Policy creation exception:'
        print e
        print ' '

#============ Create Roles ================
def createRoles():
    rm=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/RoleMappers/XACMLRoleMapper')

    i=0
    print 'creating roles'
    roles = ['user','creator']
    groups = ['AuctionUsers', 'AuctionCreators']
    for role in roles:
        try:
            print 'creating role: ' + role
            expression = 'Grp(' + groups[i] + ')'
            rm.createRole(None, role, None)
            rm.setRoleExpression(None, role, expression)
            i += 1
            print ' '
        except Exception, e:
            print 'Role creation exception:'
            print e
            i += 1
            print ' '

#============ Create Groups ================
def createGroups():
    atnr=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/AuthenticationProviders/DefaultAuthenticator')

    i=0
    print 'creating groups'
    groups = ['AuctionUsers','AuctionCreators']
    membership = [None, None]
    for group in groups:
        try:
            print 'creating group: ' + group
            atnr.createGroup(group,'')
            if membership[i] is not None:
                print 'adding group to ' + membership[i] + ' group'
                atnr.addMemberToGroup(membership[i],group)
            i += 1
            print ' '
        except:
            print 'Group creation exception'
            i += 1
            print ' '
    


#============ Create Users ================
def createUsers():
    atnr=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/AuthenticationProviders/DefaultAuthenticator')
  
    #Password for all accounts
    password = 'Welcome1'

    i=0
    users = ['jsmith','jjones']
    membership = ['AuctionUsers','AuctionCreators']
    for user in users:     
        try:
            print 'creating user: ' + user + ' as member of group ' + membership[i]
            atnr.createUser(user,password,'')
            atnr.addMemberToGroup(membership[i],user)
            i += 1
            print ' '
        except:
            print 'User creation exception'
            i += 1
            print ' '


#============ Main Program ================
print 'Updating domain with users and groups for application'

#First WLS SM Side (both users and groups)
connectWLS('t3://host01:7001')
serverConfig()
createGroups()
createUsers()
createRoles()
createPolicy()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
