
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.container.ejb;

import com.tangosol.examples.pof.Contact;

import com.tangosol.util.MapEvent;
import com.tangosol.util.MapListener;

import java.io.FileWriter;
import java.io.IOException;

import java.util.Date;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * ContactFileWriterListener is instantiated from cache configuration to write any changes
 * to the contacts cache to a specified file.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author tam  2012.04.19
 */
public class ContactFileWriterListener
        implements MapListener {
  /**
   * No args constructor, default the file name.
   */
  public ContactFileWriterListener() {
    fileName = DEFAULT_FILE_NAME;
  }

  /**
   * Constructs a new listener to write to the given filename.
   *
   * @param sFileName filename to write out to
   */
  public ContactFileWriterListener(String fileName) {
    this.fileName = fileName;
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public void entryDeleted(MapEvent event) {
    Contact contactOld = (Contact) event.getOldValue();

    appendToFile(new Date() + " - Entry deleted: " + contactOld + "\n");
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public void entryInserted(MapEvent event) {
    Contact contactNew = (Contact) event.getNewValue();

    appendToFile(new Date() + " - Entry inserted: " + contactNew + "\n");
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public void entryUpdated(MapEvent event) {
    Contact contactOld = (Contact) event.getOldValue();
    Contact contactNew = (Contact) event.getNewValue();

    appendToFile(new Date() + " - Entry updated. Old = " + contactOld + ", New = " + contactNew + "\n");
  }

  /**
   * Append the given string to a file. If the default file name does not have a
   * path, it will be placed in the base_domain home directory.
   *
   * @param outputString string two write out to file
   */
  public void appendToFile(String outputString) {
    FileWriter out = null;

    try {
      out = new FileWriter(fileName, true);
      out.write(outputString);
      out.flush();
     }
    catch (IOException e) {
      LOGGER.log(Level.WARNING, "Error: Unable to append to file " + fileName + ": " + e.getMessage());
     }
    finally {
      try {
        out.close();
       }
      catch (IOException e) {
        // ignore file close exception
       }
     }
  }

  /**
   * HashCode is required so we can remove the {@link MapListener}.
   *
   * @return the hashCode of the object
   */
  @Override
  public int hashCode() {
    return super.hashCode() + 17;
  }

  /*
   * Default file name.
   */
  private static final String DEFAULT_FILE_NAME = "ContactFileWriterListener.log";

  /**
   * The Logger object.
   */
  private static final Logger LOGGER = Logger.getLogger(ContactFileWriterListener.class.getName());

  /*
   * File name to write output to.
   */
  private String fileName;
}
