# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host01:7001'
user = 'weblogic'
password = 'Welcome1'
server1 = 'server1'
server2 = 'dyncluster1-1'
server3 = 'dyncluster1-2'

#Connect to AdminServer and start managed servers
connect(user,password,url)
start(server1,block='true')
start(server2,block='true')
start(server3,block='true')

