
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# This script deletes the custom network channel that listens on port 4000 for HTTP traffic 

#Conditionally import wlstModule only when script is executed with jython
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

#============ Connect to server ================
def connectWLS(host):
    #WLS Must be running for this script to work
    try:
        connect('weblogic','Welcome1',host)
        print '***Connected successfully***'
    except:
        print 'Domain ' + host + ' must be running first'
        exit()

#============ Create Channel ================
def deleteNWChannel():
    try:
        server=getMBean('/Servers/server1')
        server.destroyNetworkAccessPoint(getMBean('/Servers/server1/NetworkAccessPoints/HTTPChannel'))
    except Exception, e:
        print 'Network channel creation exception:'
        print e 


#============ Main Program ================
print 'Updating domain with custom network channel'

connectWLS('t3://host01:7001')
edit()
startEdit()
deleteNWChannel()
activate()

disconnect('true')

print 'Completed update of domain...'
exit()
