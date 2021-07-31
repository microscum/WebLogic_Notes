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
public class StuckTreadsExecutor
{

  /**
   * Default constructor.
   */
  public StuckTreadsExecutor()
  {
    
  }
//  @TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
//  public void generateCpuLoad(int iterations)
//  {
//    Random random = new Random(System.currentTimeMillis());
//    BigDecimal sum = BigDecimal.ZERO;
//
//    for (int i = 0; i < iterations; i++)
//    {
//      double rnd = random.nextDouble();
//      BigDecimal bd = new BigDecimal(Math.sin(rnd), MathContext.DECIMAL64);
//      sum = sum.add(bd);
//    }
//
//    System.out.println(sum.doubleValue());
//  }
//  
  @TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
  public void generateCpuLoad(int seconds)
  {
    Random random = new Random(System.currentTimeMillis());
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
    }
    while(true);

    System.out.println(sum.doubleValue());
  }
}
