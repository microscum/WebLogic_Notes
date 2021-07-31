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
clusterName = 'cluster1'
migrationDSName = 'OracleDS1-NoXA'

server1 = 'server1'
server2 = 'server2'
server3 = 'server3'
migrationPolicy = 'failure-recovery'

# Connect to administration server
connect(username, password, url)

# Check if Cluster exists
try:
	cd('/Clusters/' + clusterName)
except WLSTException:
	print 'The Cluster ' + clusterName + ' does not exist.'
	exit()

edit()
startEdit()
cd('/')

# Get reference to leasing data source
ds = getMBean('/JDBCSystemResources/' + migrationDSName)

# Update cluster
print 'Updating leasing for Cluster named ' + clusterName + '.'
cluster = getMBean('/Clusters/' + clusterName)
cluster.setMigrationBasis('database')
cluster.setDataSourceForAutomaticMigration(ds)

# Update first migratable target
mtName = server1 + ' (migratable)'
print 'Updating Migratable Target named ' + mtName + '.'
mt = getMBean('/MigratableTargets/' + mtName)
mt.setMigrationPolicy(migrationPolicy)

# Update second migratable target
mtName = server2 + ' (migratable)'
print 'Updating Migratable Target named ' + mtName + '.'
mt = getMBean('/MigratableTargets/' + mtName)
mt.setMigrationPolicy(migrationPolicy)

# Update third migratable target
mtName = server3 + ' (migratable)'
print 'Updating Migratable Target named ' + mtName + '.'
mt = getMBean('/MigratableTargets/' + mtName)
mt.setMigrationPolicy(migrationPolicy)

# Activate changes
save()
activate(block='true')
print 'Cluster and migratable targets updated successfully.'
exit()
