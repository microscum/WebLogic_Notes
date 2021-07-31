
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.container.gar;

import com.tangosol.application.Context;
import com.tangosol.application.LifecycleListener;


public class CopyOfLifecycleReactor
        implements LifecycleListener {

	@Override
  public void preStart(Context ctx) {
    System.out.println( "LifeCycleListener:::preStart " + ctx.getExtendedContext().getApplicationName() + "\n");
  }

  @Override
  public void postStart(Context ctx) {
	    System.out.println( "LifeCycleListener:::postStart " + ctx.getExtendedContext().getApplicationName() + "\n");
  }

  @Override
  public void preStop(Context ctx) {
	    System.out.println( "LifeCycleListener:::preStop " + ctx.getExtendedContext().getApplicationName() + "\n");
  }

  @Override
  public void postStop(Context ctx) {
	    System.out.println( "LifeCycleListener:::postStop " + ctx.getExtendedContext().getApplicationName() + "\n");
  }

}
