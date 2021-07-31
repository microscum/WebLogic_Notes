# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

# Modify these values as necessary
url = 'host02:7001'
username = 'weblogic'
password = 'Welcome1'
server1 = 'server1'
server2 = 'server2'
server3 = 'server3'
JTADSName = 'OracleDS1-NoXA'
migrationPolicy = 'failure-recovery'

# Connect to administration server
connect(username, password, url)

edit()
startEdit()
cd('/')

# Get reference to JTA data source
ds = getMBean('/JDBCSystemResources/' + JTADSName)

print 'Updating JTA params for server ' + server1 + '.'
serverJTAStore = getMBean('/Servers/' + server1 + '/TransactionLogJDBCStore/' + server1)
serverJTAStore.setEnabled(true)
serverJTAStore.setDataSource(ds)
serverJTAMigration = getMBean('/Servers/' + server1 + '/JTAMigratableTarget/' + server1)
serverJTAMigration.setMigrationPolicy('failure-recovery')

print 'Updating JTA params for server ' + server2 + '.'
serverJTAStore = getMBean('/Servers/' + server2 + '/TransactionLogJDBCStore/' + server2)
serverJTAStore.setEnabled(true)
serverJTAStore.setDataSource(ds)
serverJTAMigration = getMBean('/Servers/' + server2 + '/JTAMigratableTarget/' + server2)
serverJTAMigration.setMigrationPolicy('failure-recovery')

print 'Updating JTA params for server ' + server3 + '.'
serverJTAStore = getMBean('/Servers/' + server3 + '/TransactionLogJDBCStore/' + server3)
serverJTAStore.setEnabled(true)
serverJTAStore.setDataSource(ds)
serverJTAMigration = getMBean('/Servers/' + server3 + '/JTAMigratableTarget/' + server3)
serverJTAMigration.setMigrationPolicy('failure-recovery')

# Activate changes
save()
activate(block='true')
print 'Servers updated successfully.'
exit()
