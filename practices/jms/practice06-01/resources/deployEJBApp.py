# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# ------------------------------------------------------------------------

url = 'host01:7001'
username = 'weblogic'
password = 'Welcome1'
appName = 'ConsumerEJBApp'
appSource = '/practices/jms/practice03-01/resources/ConsumerEJBApp.jar'
target = 'server1'

# Connect to administration server
connect(username, password, url)

print '>>>Deploying application ' + appName + ' to ' + target
print ''
deploy(appName=appName,path=appSource,targets=target)
