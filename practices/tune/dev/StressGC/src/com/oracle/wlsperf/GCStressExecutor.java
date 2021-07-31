package com.oracle.wlsperf;

import javax.ejb.Asynchronous;
import javax.ejb.LocalBean;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Session Bean implementation
 */
@Stateless
@LocalBean
@Asynchronous
public class GCStressExecutor
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
  private Random random = null;

  /**
   * Default constructor.
   */
  public GCStressExecutor()
  {
    buf = new char[225];
  }

  private String nextString()
  {
      for (int idx = 0; idx < buf.length; ++idx)
          buf[idx] = symbols[random.nextInt(symbols.length)];
      return new String(buf);
  }  
  
  @TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
  public void generateGarbageCollectionActivity(int seconds)
  {
    List<String> repository = new ArrayList<String>();
    Random random = new Random(System.currentTimeMillis());

    long start = System.currentTimeMillis();
    long stop = start + (seconds * 1000);
    do
    {
      int howMany = 10 + random.nextInt(10000);
      for(int ii = 0; ii < howMany; ii++)
      {
        String s = nextString();
        repository.add(s);
      }
      repository.clear();
      long now = System.currentTimeMillis();
      if (now > stop)
      {
        break;
      }
    }
    while (true);
  }
}
