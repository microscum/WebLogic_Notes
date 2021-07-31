package com.oracle.wlsperf;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Random;

import org.apache.log4j.Logger;

public class SocketProcessor implements Runnable
{
	private static final char[] symbols = new char[36];

	static
	{
		for (int idx = 0; idx < 10; ++idx)
			symbols[idx] = (char) ('0' + idx);
		for (int idx = 10; idx < 36; ++idx)
			symbols[idx] = (char) ('a' + idx - 10);
	}
	private final char[] buf;
	private final Socket socket;
	private DataInputStream dis;
	private DataOutputStream dos;
	private Random random = null;
	private static final Logger log = Logger.getLogger(SocketProcessor.class);
	public SocketProcessor(Socket  socket)
	{
		this.socket = socket;
		buf = new char[36];
		this.random = new Random(System.currentTimeMillis());
	}
	@Override
	public void run()
	{
		try
		{
			dis = new DataInputStream(this.socket.getInputStream());
			dos = new DataOutputStream(this.socket.getOutputStream());
			byte[] impHeader = new byte[8];
			while(true)
			{
				dis.readFully(impHeader);
				int howManyStrings = Integer.parseInt(new String(impHeader));
				if(howManyStrings == 0)
				{
					break;
				}
				StringBuffer sb = new StringBuffer();
				for(int ii = 0; ii < howManyStrings; ii++)
				{
					sb.append(this.nextString());
					sb.append('\n');
				}
				String toBeSent = sb.toString();
				byte [] packet=this.assemblePacket(toBeSent);
				dos.write(packet);
			}
			this.socket.close();
			return;
		}
		catch (IOException e)
		{
			log.error(e);
		}
	}

	private String nextString()
	{
		for (int idx = 0; idx < buf.length; ++idx)
			buf[idx] = symbols[random.nextInt(symbols.length)];
		return new String(buf);
	}

	private byte[] assemblePacket(String toBeSent)
	{
		int len = toBeSent.length();
		String lstr = String.format("%08d", len);
		StringBuffer sb = new StringBuffer(lstr);
		sb.append(toBeSent);
		byte[] packet = sb.toString().getBytes();
		return packet;
	}
}
