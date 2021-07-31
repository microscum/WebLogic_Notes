These steps were used to install and configure Apache JMeter for a JMS load test:

1. unzip -q apache-jmeter-2.9.zip -d /practices/jms/jmeter
2. cp /u01/app/fmw/wlserver/server/lib/wljmsclient.jar /practices/jms/jmeter/lib
3. cp /u01/app/fmw/wlserver/server/lib/wlclient.jar /practices/jms/jmeter/lib
4. chmod +x /practices/jms/jmeter/bin/jmeter
5. Run /practices/jms/jmeter/bin/jmeter
6. Right-click Test Plan and click Add > Threads > Thread Group
7. Set Number of Threads to 5 and Loop Count to Forever
8. Right-click Thread Group and click Add > Logic Controller > Throughput Controller
9. Set Throughput to 20
10. Right-click Throughput Controller and click Add > Timer > Constant Throughput Timer
11. Set Target Throughput to 60 and Calculate Throughput based on all active threads in current thread group
12. Right-click Throughput Controller and click Add > Sampler > JMS Point to Point
13. Set these fields:
    QueueConnectionFactory = jms.example.Factory1
    JNDI name Request queue = jms.example.Queue1
    Content = This test message was generated from Apache JMeter
    Initial Context Factory = weblogic.jndi.WLInitialContextFactory
    Provider URL = t3://host01:7011
    Right-click Throughput Controller and click Add > Listener > Summary Report
14. Save as TestPlan.jmx




