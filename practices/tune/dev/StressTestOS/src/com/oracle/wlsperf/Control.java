package com.oracle.wlsperf;

import java.util.ArrayList;
import java.util.List;

public class Control implements ControlMBean
{
	private List<Stoppable> stoppableThreads;
	
	private StressTestOS sto;
	private String remoteHost;
	private int remotePort;
	
	public Control(StressTestOS sto)
	{
		this.sto = sto;
		this.stoppableThreads = new ArrayList<Stoppable>();
		this.remoteHost = "host02.example.com";
		this.remotePort = 9090;
	}
	@Override
	public void stressCPU(int threads)
	{
		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();
		for(int ii = 0; ii< threads; ii++)
		{
			StressTestCPU stcp = new StressTestCPU(this.sto);
			this.stoppableThreads.add(stcp);
			this.sto.submit(stcp);
		}
	}
	@Override
	public void stopCPUStress()
	{

		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();
	}
	@Override
	public void stressDisk(int threads)
	{
		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();
		for(int ii = 0; ii< threads; ii++)
		{
			String fnm = "file_"+ii+"_random";
			StressTestDisk std = new StressTestDisk(fnm);
			this.stoppableThreads.add(std);
			this.sto.submit(std);
		}
		
	}
	@Override
	public void stopDiskStress()
	{
		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();		
	}
	
	@Override
	public void stressNetwork(int threads)
	{
		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();
		for(int ii = 0; ii< threads; ii++)
		{
			StressTestNet stn = new StressTestNet(this.remoteHost, this.remotePort);
			this.stoppableThreads.add(stn);
			this.sto.submit(stn);
		}
	}
	@Override
	public void stopNetworkStress()
	{
		for(Stoppable stop : this.stoppableThreads)
		{
			stop.stop_run();
		}
		this.stoppableThreads.clear();
	}
	@Override
	public void requestShutdown()
	{
		this.sto.setRunning(false);
		
	}
	@Override
	public String getRemoteHost()
	{
		
		return this.remoteHost;
	}
	@Override
	public void setRemoteHost(String host)
	{
		this.remoteHost = host;
		
	}
	@Override
	public int getRemotePort()
	{
		
		return this.remotePort;
	}
	@Override
	public void setRemotePort(int port)
	{
		this.remotePort = port;
		
	}
}
