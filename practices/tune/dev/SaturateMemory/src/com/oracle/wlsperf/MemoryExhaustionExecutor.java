package com.oracle.wlsperf;

import javax.ejb.Asynchronous;
import javax.ejb.LocalBean;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import java.math.BigDecimal;
import java.math.MathContext;
import java.util.Random;

/**
 * Session Bean implementation class StuckTreadsExecutor
 */
@Stateless
@LocalBean
@Asynchronous
public class MemoryExhaustionExecutor
{

  /**
   * Default constructor.
   */
  public MemoryExhaustionExecutor()
  {
    
  }

  @TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
  public void generateMemoryLoad(long memoryAmount, int seconds)
  {
    Random random = new Random(System.currentTimeMillis());
    int howMany = (int) memoryAmount / 8;
    long [] arr =  new long[howMany];
    for(int jj = 0; jj < howMany; jj++)
    {
      arr[jj]= random.nextLong();
    }
    BigDecimal sum = BigDecimal.ZERO;
    long start = System.currentTimeMillis();
    long stop = start + (seconds * 1000);
    do
    {
      double rnd = random.nextDouble();
      BigDecimal bd = new BigDecimal(Math.sin(rnd), MathContext.DECIMAL64);
      sum = sum.add(bd);
      long now = System.currentTimeMillis();
      if(now > stop )
      {
        break;
      }
      for(int jj = 0; jj < howMany; jj++)
      {
        arr[jj]= random.nextLong();
      }
    }
    while(true);
  }
}
