
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script updates the OES WLS SM domain's embedded LDAP with the users and groups needed
# to run the Trader application. OES WLS SMs use the embedded LDAP of their own domain

import sys
import os


#============ Connect to server ================
def connectWLS(host):
  #WLS Must be running for this script to work
  try:
    connect('weblogic','Welcome1',host)
    print '***Connected successfully***'
  except:
    print 'Domain ' + host + ' must be running first'
    exit()


#============ Create Groups ================
def createGroups():
  serverConfig()

  atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')

  i=0
  print 'creating groups'
  groups = ['AuctionUser','AuctionCreators']
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
  serverConfig()

  atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
  
  #Password for all accounts
  password = 'Welcome1'

  i=0
  users = ['jsmith','jjones']
  membership = ['AuctionUser','AuctionCreators']
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
createGroups()
createUsers()

#Disconnect
disconnect('true')

print 'Completed update of domain...'
exit()
