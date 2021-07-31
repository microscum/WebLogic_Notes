package com.oracle.wlsperf;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.File;
import java.util.Random;

import org.apache.log4j.Logger;

public class StressTestDisk implements Runnable, Stoppable
{
	private static final char[] symbols = new char[36];

	static
	{
		for (int idx = 0; idx < 10; ++idx)
			symbols[idx] = (char) ('0' + idx);
		for (int idx = 10; idx < 36; ++idx)
			symbols[idx] = (char) ('a' + idx - 10);
	}
	private static final Logger log = Logger.getLogger(StressTestDisk.class);
	private final char[] buf;
	private String tmpDir = "/tmp";
	private boolean running = true;
	private String fname;
	private Random random = null;
	private PrintWriter pw = null;
	private int counter = 0;

	public StressTestDisk(String filename)
	{
		this.fname = filename;
		buf = new char[36];
		this.random = new Random(System.currentTimeMillis());
	}

	@Override
	public void stop_run()
	{
		this.running = false;
		if (this.pw != null)
		{
			this.pw.close();
		}
		log.info(""+hashCode()+": Termination requested");
	}

	@Override
	public void run()
	{
		log.info(""+hashCode()+": Started running");
		File f = new File(tmpDir + "/" + this.fname+".txt");

		try
		{
			pw = new PrintWriter(f);
		}
		catch (FileNotFoundException e)
		{
			// TODO Auto-generated catch block
			log.error(e);
			return;
		}
		log.info("Created file: " + f.getAbsolutePath());
		do
		{
			String randomStr = this.nextString();
			pw.println(randomStr);
			counter++;
			if ((counter % 1000) == 0)
			{
				try
				{
					Thread.sleep(20);
				}
				catch (InterruptedException e1)
				{
					// Do noting
				}
			}
		}
		while (running);
	}

	private String nextString()
	{
		for (int idx = 0; idx < buf.length; ++idx)
			buf[idx] = symbols[random.nextInt(symbols.length)];
		return new String(buf);
	}
}
