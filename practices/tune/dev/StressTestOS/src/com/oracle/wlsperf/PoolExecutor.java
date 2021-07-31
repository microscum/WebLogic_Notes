package com.oracle.wlsperf;

import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import org.apache.log4j.*;

public class PoolExecutor
{
	private ExecutionEnvironment tpe;
	@SuppressWarnings("unused")
	private StressTestOS sto;
	private static final Logger log = Logger.getLogger(PoolExecutor.class);
	
	public PoolExecutor(StressTestOS sto, int poolSize, int maxPoolSize)
	{
		tpe = new ExecutionEnvironment(poolSize, maxPoolSize, 50000L,
				TimeUnit.SECONDS, new LinkedBlockingQueue<Runnable>(), sto);
		this.sto = sto;
	}
	
	public void execute(Runnable runnable)
	{
		this.tpe.execute(runnable);
		log.debug("Submitted task: "+runnable.hashCode());
	}
}
