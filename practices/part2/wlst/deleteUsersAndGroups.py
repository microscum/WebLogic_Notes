
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
  serverConfig()
  atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
  print 'deleting users'
  users = ['jsmith','jjones']
  for user in users:
    print 'deleting user: ' + user
    try:
      atnr.removeUser(user)
    except:
      print 'User deletion exception'

def deleteGroups():
  serverConfig()
  atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')
  print 'deleting groups'
  groups = ['AuctionUser','AuctionCreators']
  for group in groups:
    print 'deleting group: ' + group
    try:
      atnr.removeGroup(group)
    except:
      print 'Group deletion exception'

#Delete stuff
connectWLS('t3://localhost:6001')
deleteUsers()
deleteGroups()

#Disconnect
disconnect('true')

exit()
