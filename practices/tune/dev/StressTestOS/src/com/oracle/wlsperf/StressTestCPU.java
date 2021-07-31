package com.oracle.wlsperf;

import org.apache.log4j.Logger;

public class StressTestCPU implements Stoppable, Runnable
{
	private long counter = 0;
	private boolean running = true;
	@SuppressWarnings("unused")
	private StressTestOS sto;
	private static final Logger log = Logger
			.getLogger(StressTestCPU.class);
	@Override
	public void stop_run()
	{
		this.running = false;
		log.info(""+hashCode()+": Termination requested");
	}

	public StressTestCPU(StressTestOS sto)
	{
		this.sto = sto;
	}

	@Override
	public void run()
	{
		log.info(""+hashCode()+": Started running");
		this.do_test();
	}

	private double km(double paramDouble)
	{
		if (paramDouble <= 1.0D)
		{
			return 1.0D;
		}

		return paramDouble * km(paramDouble - 1.0D);
	}

	private double euklides(double paramDouble1, double paramDouble2)
	{
		if ((paramDouble1 > 0.0D) && (paramDouble2 > 0.0D))
		{
			do
			{
				if (paramDouble1 < paramDouble2)
				{
					double d = paramDouble2;
					paramDouble2 = paramDouble1;
					paramDouble1 = d;
				}
				paramDouble1 %= paramDouble2;
			}
			while (paramDouble1 != 0.0D);
			return paramDouble2;
		}
		return 0.0D;
	}

	@SuppressWarnings("unused")
	public void do_test()
	{

		double d2;
		double d3;
		double d4;
		double d5;
		double d6;
		double d7;
		do
		{
			double d9 = km(162.0D);
			double d10 = km(152.0D);
			double d11 = d10 * Math.pow(0.99843D, 9999.0D);
			double d12 = d9 * Math.pow(0.93853D, 9939.0D);
			double d13 = Math.pow(99.328673551999998D, 99.0D)
					* (d10 * Math.pow(0.934543553D, 9989.0D) * 0.01532567342345346D);
			double d14 = Math.pow(99.082374325000004D, 99.0D)
					* (d9 * Math.pow(0.923453443D, 9979.0D) * 0.01452345535456758D);
			double d15 = (d11 * 0.928378465273659D * (d12 * 2.0D) / 3414.0D
					* 0.1231415235363644D + d13 + d14) * 0.01298407582375926D;
			double d1 = d15 * 0.03483826486283644D;
			double d16 = km(161.0D);
			double d17 = km(153.0D);
			double d18 = km(159.0D);
			double d19 = km(153.0D);
			double d20 = km(158.0D);
			double d21 = km(157.0D);
			double d22 = km(156.0D);
			double d23 = km(154.0D);
			double d24 = km(156.0D);
			double d25 = km(154.0D);
			double d26 = km(156.0D);
			double d27 = km(154.0D);
			d2 = euklides(d16, d17);
			d3 = euklides(d18, d19);
			d4 = euklides(d20, d21);
			d5 = euklides(d22, d23);
			d6 = euklides(d22, d23);
			d7 = euklides(d22, d23);
			double d8 = d2 / d3 / d4 / d5 / d6 / d7;
			double e = d2 + d3 + d4 + d5 + d6 + d7;
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
		// while (d2 + d3 + d4 + d5 + d6 + d7 == 4.7233217434187173E263D);
		while (running);
	}

	public long getCounter()
	{
		return counter;
	}
}
