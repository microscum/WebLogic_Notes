package com.oracle.wlsperf;


import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

public class ExecutionEnvironment extends ThreadPoolExecutor
{
	private StressTestOS sto;
	public ExecutionEnvironment(int poolSize, int maxPoolSize, long ts, TimeUnit seconds, LinkedBlockingQueue<Runnable> queue, StressTestOS sto)
	{
		super(poolSize,maxPoolSize,ts,seconds,queue);
		this.sto = sto;
	}
	
	protected void terminated()
	{
		super.terminated();
		this.sto.setExecutionTerminated(true);
	}
}