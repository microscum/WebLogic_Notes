
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

import sys
import os
import weblogic.security.service.URLResource


#============ Connect to server ================
def connectWLS(host):
    #WLS Must be running for this script to work
    try:
        connect('weblogic','Welcome1',host)
        print '***Connected successfully***'
    except:
        print 'Domain ' + host + ' must be running first'
        exit()



def deleteUsers():
    atnr=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/AuthenticationProviders/DefaultAuthenticator')
    print 'deleting users'
    users = ['jsmith','jjones']
    for user in users:
        print 'deleting user: ' + user
        try:
            atnr.removeUser(user)
        except:
            print 'User deletion exception'

def deleteGroups():
    atnr=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/AuthenticationProviders/DefaultAuthenticator')
    print 'deleting groups'
    groups = ['AuctionUsers','AuctionCreators']
    for group in groups:
        print 'deleting group: ' + group
        try:
            atnr.removeGroup(group)
        except:
            print 'Group deletion exception'

def deleteRoles():
    rm=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/RoleMappers/XACMLRoleMapper')
    print 'deleting roles'
    roles = ['user','creator']
    for role in roles:
        print 'deleting role: ' + role
        try:
            rm.removeRole(None, role)
        except Exception, e:
            print 'Role deletion exception:'
            print e

def deletePolicies():
    authz=getMBean('/SecurityConfiguration/wlsadmin/DefaultRealm/myrealm/Authorizers/XACMLAuthorizer')
    print 'deleting policies'
    #URLResource(application, context_path, pattern, httpMethod, transport)
    r=weblogic.security.service.URLResource('SimpleAuctionWebAppDbSec','/SimpleAuctionWebAppDbSec','/createAuction.jsp',None,None)
    resourceID=r.toString()
    try:
        authz.removePolicy(resourceID)    
    except Exception, e:
        print 'Policy deletion exception:'
        print e

#Delete stuff
connectWLS('t3://host01:7001')
serverConfig()
deletePolicies()
deleteRoles()
deleteUsers()
deleteGroups()

#Disconnect
disconnect('true')

exit()
