# Adds users to the embedded LDAP
# By: ST Curriculum Development Team
# Version 1.0
# Last updated: Nov 14, 2013
#
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# variables
url = 't3://host01.example.com:7001'
username = 'weblogic'
password = 'Welcome1'
realmname = 'myrealm'
providername = 'DefaultAuthenticator'
domainname = 'wlsadmin'
user1 = 'fred'
user2 = 'wilma'
groupname = 'Administrators'

# Connect to administration server
connect(username, password, url)

found = false

# locate the authentication provider
try:
	cd('/SecurityConfiguration/' + domainname + '/Realms/' + realmname + '/AuthenticationProviders/' + providername)
	provider = getMBean('/SecurityConfiguration/' + domainname + '/Realms/' + realmname + '/AuthenticationProviders/' + providername)
	found = true
except WLSTException:
	pass

# create users if auth provider there
if(found):
	print '>>>Adding users ' + user1 + ' and ' + user2 + '.'
	print '>>>Giving them both the password: ' + password + '.'
	print '>>>Placing users in the group ' + groupname + '.'
	try:
		provider.createUser(user1, password, user1 + ' the admin')
		provider.addMemberToGroup(groupname, user1)
		provider.createUser(user2, password, user2 + ' the admin')
		provider.addMemberToGroup(groupname, user2)
	except weblogic.management.utils.AlreadyExistsException:
		pass
	print '>>>Users created successfully.'
else:
	print '>>>Authorization provider not found.'

exit()

