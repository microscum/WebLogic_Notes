
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
    
# Modify these values as necessary
url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
wmNames = ['HighPriorityWM','LowPriorityWM']
rqNames = ['FairShare90','FairShare10']
rqFairShare = [90,10]
targetName = 'cluster1'
domainName = 'wlsadmin'

# Connect to administration server
connect(username, password, url)

edit()
startEdit()
stMBean=getMBean("/SelfTuning/" + domainName)
for workManager in wmNames:
    wmMBean=getMBean("/SelfTuning/" + domainName + "/WorkManagers/" + workManager)
    if wmMBean != None:
        stMBean.destroyWorkManager(wmMBean)
        print "destroyed work manager " + workManager

for fairShare in rqNames:
    fsMBean=getMBean("/SelfTuning/" + domainName + "/FairShareRequestClasses/" + fairShare)
    if fsMBean != None:
        stMBean.destroyFairShareRequestClass(fsMBean)
        print "destroyed fair share request class " + fairShare
 
#Activate changes, if any
save()
activate(block='true')
print 'Work Managers deleted successfully.'




