
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.container.ejb;

import com.tangosol.net.CacheFactory;
import com.tangosol.net.NamedCache;

import com.tangosol.util.MapListener;

import java.util.logging.Level;
import java.util.logging.Logger;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import javax.ejb.Singleton;
import javax.ejb.Startup;

/**
 * This class uses {@link Singleton} and {@link Startup} annotations as defined
 * in the EJB 3.1 specification. On startup this class will register a
 * {@link MapListener} implementation ({@link ContactFileWriterListener}) on a
 * {@link NamedCache} which is responsible for logging all received events to an
 * output file.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author tam  2012.04.23
 */

@Singleton
@Startup
public class SingletonFileWriterStartupBean {
  /**
   * Constructs a new {@SingletonFileWriterStartupBean}.
   *
   */
  public SingletonFileWriterStartupBean() {
  }

  /**
   * This is called at startup by the Java EE container. The method will create
   * a {@link MapListener} and register it with the cache.
   */
  @PostConstruct
  public void atStartup() {
    if (LOGGER.isLoggable(Level.INFO)) {
      LOGGER.log(Level.INFO, "AddingMap Listener to contacts cache");
    }

    cacheContacts = CacheFactory.getCache(CACHE_NAME);
    listener      = new ContactFileWriterListener();
    cacheContacts.addMapListener(listener);

  }

  /**
   * This method is called before shutdown to remove the added {@link MapListener}.
   */
  @PreDestroy
  public void atShutdown() {
    if (LOGGER.isLoggable(Level.INFO)) {
      LOGGER.log(Level.INFO, "Removing MapListener from contacts cache");
    }

    cacheContacts.removeMapListener(listener);

    if (LOGGER.isLoggable(Level.INFO)) {
      LOGGER.log(Level.INFO, "MapListener removed");
    }

  }

  /**
   * The Logger object.
   */
  private static final Logger LOGGER = Logger.getLogger(SingletonFileWriterStartupBean.class.getName());

  /**
   * Coherence cache name to use.
   */
  public static final String CACHE_NAME = "contacts";

  private NamedCache         cacheContacts;
  private MapListener        listener;
}
