package com.oracle.wlsperf;

import org.apache.log4j.Logger;
import java.io.*;
import java.net.*;
import java.util.Random;

public class StressTestNet implements Runnable, Stoppable
{
	private Socket socket;
	private String host;
	private int port;
	private Random random = null;
	private DataInputStream dis;
	private DataOutputStream dos;
	private boolean running = true;
	
	private static final Logger log = Logger.getLogger(StressTestNet.class);
	
	public StressTestNet(String host, int port)
	{
		this.host = host;
		this.port = port;
		this.random = new Random(System.currentTimeMillis());
	}
	
	@Override
	public void stop_run()
	{
		this.running = false;
		log.info(""+hashCode()+": Termination requested");
	}

	@Override
	public void run()
	{
		try
		{
			this.socket = new Socket(this.host, this.port);
			dis = new DataInputStream(this.socket.getInputStream());
			dos = new DataOutputStream(this.socket.getOutputStream());			
			byte[] impHeader = new byte[8];
			
			do
			{
				int howManyStrings = 1 + this.random.nextInt(50);
				String lstr = String.format("%08d", howManyStrings);
				byte [] packet = lstr.getBytes();
				dos.write(packet);
				dis.readFully(impHeader);
				int howManyBytes = Integer.parseInt(new String(impHeader));
				byte [] readStream = new byte[howManyBytes];
				dis.readFully(readStream);
				//log.info("Read " + readStream.length+" bytes from server");
			}
			while(this.running);
			String lstr = String.format("%08d", 0);
			byte [] packet = lstr.getBytes();
			dos.write(packet);
			this.socket.close();
			return;
		}
		catch(UnknownHostException  uhe)
		{
			log.error(uhe);
		}
		catch(IOException  ioe)
		{
			log.error(ioe);
		}
	}

}
