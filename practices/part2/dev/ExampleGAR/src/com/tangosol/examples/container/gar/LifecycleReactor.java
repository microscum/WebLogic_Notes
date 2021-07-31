
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

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * LifecycleReactor is called on start/stop of container to perform an initializing or
 * post processing actions.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author tam  2012.05.19
 */
public class LifecycleReactor
        implements LifecycleListener {
  /**
   * LifecycleReactor is called on startup and shutdown of the container providing
   * a callback for any initialization or shutdown code.
   *
   * @param ctx the {@link Context} in which the container is running
   */
  @Override
  public void preStart(Context ctx) {
    LOGGER.log(Level.ALL, "[LC::preStart] " + ctx.getExtendedContext().getApplicationName());
  }

  /**
   * Defines any actions to call after the container is started. For the purposes
   * of this example, a message is logged to the default {@Logger}.
   *
   * @param ctx the {@link Context} in which the container is running
   */
  @Override
  public void postStart(Context ctx) {
    LOGGER.log(Level.ALL, "[LC::postStart] " + ctx.getExtendedContext().getApplicationName());
  }

  /**
   * Defines any actions to call before the container is stopped. For the purposes
   * of this example, a message is logged to the default {@Logger}.
   *
   * @param ctx the {@link Context} in which the container is running
   */
  @Override
  public void preStop(Context ctx) {
    LOGGER.log(Level.ALL, "[LC::preStop] " + ctx.getExtendedContext().getApplicationName());
  }

  /**
   * Defines any actions to call after the container is stopped. For the purposes
   * of this example, a message is logged to the default {@Logger}.
   *
   * @param ctx the {@link Context} in which the container is running
   */
  @Override
  public void postStop(Context ctx) {
    LOGGER.log(Level.ALL, "[LC::postStop] " + ctx.getExtendedContext().getApplicationName());
  }

  /**
   * The Logger object.
   */
  private final static Logger LOGGER = Logger.getLogger(LifecycleReactor.class.getName());
}
