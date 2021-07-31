
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


cd('/Clusters/cluster1')
cmo.setCoherenceClusterSystemResource(None)

cd('/CoherenceClusterSystemResources/ManagedCoherenceCluster')
cmo.removeTarget(getMBean('/Clusters/cluster1'))

cd('/Clusters/cluster1')
cmo.setCoherenceClusterSystemResource(getMBean('/CoherenceClusterSystemResources/CoherenceCluster1'))

cd('/CoherenceClusterSystemResources/CoherenceCluster1')
cmo.addTarget(getMBean('/Clusters/cluster1'))

activate()

startEdit()

cd('/')
cmo.destroyCoherenceClusterSystemResource(getMBean('/CoherenceClusterSystemResources/ManagedCoherenceCluster'))

activate()
