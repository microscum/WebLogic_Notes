
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


cd('/')
cmo.createCoherenceClusterSystemResource('ManagedCoherenceCluster')

cd('/CoherenceClusterSystemResources/ManagedCoherenceCluster/CoherenceClusterResource/ManagedCoherenceCluster/CoherenceClusterParams/ManagedCoherenceCluster')
cmo.setClusteringMode('unicast')
cmo.setUnicastListenPort(0)

cd('/Clusters/cluster1')
cmo.setCoherenceClusterSystemResource(getMBean('/CoherenceClusterSystemResources/ManagedCoherenceCluster'))

cd('/CoherenceClusterSystemResources/ManagedCoherenceCluster')
cmo.addTarget(getMBean('/Clusters/cluster1'))

cd('/Servers/server1/CoherenceMemberConfig/server1')
cmo.unSet('UnicastListenPort')
cmo.setLocalStorageEnabled(false)

activate()
