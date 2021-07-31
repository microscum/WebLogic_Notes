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
machineName1 = 'machine1'
machineName2 = 'machine2'

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

# Get reference to candidate machines
machine1 = getMBean('/Machines/' + machineName1)
machine2 = getMBean('/Machines/' + machineName2)

# Get reference to leasing data source
ds = getMBean('/JDBCSystemResources/' + migrationDSName)

# Update cluster
print 'Updating Cluster named ' + clusterName + '.'
cluster = getMBean('/Clusters/' + clusterName)
cluster.setMigrationBasis('database')
cluster.setDataSourceForAutomaticMigration(ds)
cluster.setCandidateMachinesForMigratableServers(jarray.array([machine1,machine2], machine1.getClass()))

# Activate changes
save()
activate(block='true')
print 'Cluster updated successfully.'
exit()
