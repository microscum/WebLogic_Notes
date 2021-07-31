package com.oracle.wlsperf;

public interface ControlMBean 
{
	public void requestShutdown();
	public void stressCPU(int threads);
	public void stopCPUStress();
	public void stressDisk(int threads);
	public void stopDiskStress();
	public void stressNetwork(int threads);
	public void stopNetworkStress();
	public String getRemoteHost();
	public void setRemoteHost(String host);
	public int getRemotePort();
	public void setRemotePort(int port);
}
