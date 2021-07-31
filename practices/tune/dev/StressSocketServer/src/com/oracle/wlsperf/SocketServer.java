package com.oracle.wlsperf;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.log4j.PatternLayout;
import org.apache.log4j.RollingFileAppender;

public class SocketServer
{
	private int socketServerPort = 0;
	final ExecutorService clientProcessingPool = Executors
			.newFixedThreadPool(10);
	private String debugLevel = "DEBUG";
	private String logDir = "/tmp";
	private static final Logger log = Logger.getLogger(SocketServer.class);
	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		int port = 0;
		if (args.length > 0)
		{
			try
			{
				port = Integer.parseInt(args[0]);
			}
			catch (NumberFormatException nfe)
			{
				System.err.println("Incorrect socket port number. Exiting...");
				System.exit(-1);
			}
		}
		if (port == 0)
		{
			port = 9090;
		}
		SocketServer ss = new SocketServer(port);
		ss.initLog();
		ss.execute();
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
					this.logDir + dirsep.trim() + "SocketServer.log");
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
	public SocketServer(int port)
	{
		this.socketServerPort = port;
	}

	public void execute()
	{
		int counter = 1;
		try
		{
			ServerSocket serverSocket = new ServerSocket(this.socketServerPort);
			System.out.println("Waiting for clients to connect...");
			while (true)
			{
				Socket clientSocket = serverSocket.accept();
				clientProcessingPool.submit(new SocketProcessor(clientSocket));
				System.out.println("Accepted Connection: "+counter);
				counter++;
			}
		}
		catch (IOException e)
		{
			System.err.println("Unable to process client request");
			log.error(e);

		}
	}

}
