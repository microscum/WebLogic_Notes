package com.oracle.wlsperf;

import java.io.IOException;
import java.lang.management.ManagementFactory;


import javax.management.*;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.log4j.PatternLayout;
import org.apache.log4j.RollingFileAppender;

public class StressTestOS
{
	private boolean executionTerminated = false;
	private boolean running = true;
	private MBeanServer mbs = null;
	private PoolExecutor pe;
	private ObjectName controlName;
	private Control controlBean;
	private String debugLevel = "DEBUG";
	private String logDir = "/tmp";
	private static final Logger log = Logger
			.getLogger(StressTestOS.class);
	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		StressTestOS sto = new StressTestOS();
		sto.initLog();
		sto.initialize();
		sto.exec();
	}

	public boolean isExecutionTerminated()
	{
		return executionTerminated;
	}

	public void setExecutionTerminated(boolean executionTerminated)
	{
		this.executionTerminated = executionTerminated;
	}
	
	@SuppressWarnings("static-access")
	private void exec()
	{
		System.out.println("StressTestOS started...");
		while (this.running)
		{
			try
			{
				Thread.currentThread().sleep(5000);
			}
			catch (InterruptedException e)
			{
				log.error(e);
			}
		}
		System.exit(0);
	}
	
	private void initLog()
	{
		String dirsep = System.getProperty("file.separator");
		Logger rootLogger = Logger.getRootLogger();
		if (this.debugLevel.equalsIgnoreCase("INFO"))
		{
			rootLogger.setLevel(Level.INFO);
		}
		else if (this.debugLevel.equalsIgnoreCase("DEBUG"))
		{
			rootLogger.setLevel(Level.DEBUG);
		}
		PatternLayout layout = new PatternLayout(
				"%d{ISO8601} [%t] %-5p %c %x - %m%n");
		// rootLogger.addAppender(new ConsoleAppender(layout));

		try
		{
			RollingFileAppender rfa = new RollingFileAppender(layout,
					this.logDir + dirsep.trim() + "StressTestOS.log");
			rfa.setMaximumFileSize(100000000);
			rfa.setMaxBackupIndex(30);
			rootLogger.addAppender(rfa);

		}
		catch (IOException e)
		{
			e.printStackTrace();
			System.exit(-1);
		}

		log.info("Logging Initialized...");
	}
	public void submit(Runnable runnable)
	{
		this.pe.execute(runnable);
	}
	private void initialize()
	{
		this.pe = new PoolExecutor(this,10,50);
		this.mbs = ManagementFactory.getPlatformMBeanServer();
		this.controlBean = new Control(this);
		try
		{
			this.controlName = new ObjectName("StressTestOSAgent:name=controlbn");
			mbs.registerMBean(this.controlBean, this.controlName);
		}
		catch (InstanceAlreadyExistsException e)
		{
			log.error(e);
		}
		catch (MBeanRegistrationException e)
		{
			log.error(e);
		}
		catch (NotCompliantMBeanException e)
		{
			log.error(e);
		}
		catch (MalformedObjectNameException e)
		{
			log.error(e);
		}
		catch (NullPointerException e)
		{
			log.error(e);
		}
	}

	public void setRunning(boolean running)
	{
		this.running = running;
		log.info("Shutdown requested");
	}
}
