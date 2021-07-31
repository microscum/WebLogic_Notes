
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.container.gui.maplistener;

import com.tangosol.examples.container.gui.ContactListenerGUI;
import com.tangosol.examples.pof.Contact;

import com.tangosol.util.Base;
import com.tangosol.util.MapEvent;
import com.tangosol.util.MapListener;

import java.text.Format;
import java.text.SimpleDateFormat;

import java.util.Date;

/**
 * This {@link MapListener} responds to events on the contacts cache and displays information
 * about those events.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author tam  2012.04.30
 */
public class ContactMapListener
        implements MapListener {
  /**
   * Construct the {@link ContactMapListener}.
   *
   * @param gui the {@link ContactListenerGUI} that is to be updated by this {@link MapListener}
   */
  public ContactMapListener(ContactListenerGUI gui) {
    this.gui = gui;

    gui.getTxtLastEventDetails().setText("Map Listener Started.");
    gui.getTxtEventCount().setText(String.valueOf(gui.getEventCount()).toString());

  }

  /**
   * Handle the delete event
   *
   * @param event {@link MapEvent} raised from the delete event
   */
  @Override
  public void entryDeleted(MapEvent event) {
    Contact oldContact = (Contact) event.getOldValue();

    gui.getTxtLastEvent().setText("Deleted");
    gui.getTxtLastEventDetails().setText("");
    gui.getEventCount().incrementAndGet();

    displayContactDetails(oldContact);
  }

  /**
   * Handle the insert event.
   *
   * @param event {@link MapEvent} raised from the insert event
   */
  @Override
  public void entryInserted(MapEvent event) {
    Contact newContact = (Contact) event.getNewValue();

    gui.getTxtLastEvent().setText("Inserted");
    gui.getTxtLastEventDetails().setText("");
    gui.getEventCount().incrementAndGet();

    displayContactDetails(newContact);
  }

  /**
   * Handle the update event.
   *
   * @param event {@link MapEvent} raised from the update event
   */
  @Override
  public void entryUpdated(MapEvent event) {
    Contact oldContact = (Contact) event.getOldValue();
    Contact newContact = (Contact) event.getNewValue();
    
    gui.getEventCount().incrementAndGet();

    gui.getTxtLastEvent().setText("Updated");
    displayContactDetails(newContact);

    // now figure out what changed
    StringBuilder sb = new StringBuilder();

    appendOnUpdate(sb, oldContact.getLastName(), newContact.getLastName(), "Last Name");
    appendOnUpdate(sb, oldContact.getFirstName(), newContact.getFirstName(), "First Name");
    appendOnUpdate(sb, oldContact.getBirthDate(), newContact.getBirthDate(), "Birth Date");
    appendOnUpdate(sb, oldContact.getHomeAddress(), newContact.getHomeAddress(), "Home Address");
    appendOnUpdate(sb, oldContact.getWorkAddress(), newContact.getWorkAddress(), "Work Address");
    appendOnUpdate(sb, oldContact.getHomePhone(), newContact.getHomePhone(), "Home Phone");
    appendOnUpdate(sb, oldContact.getWorkPhone(), newContact.getWorkPhone(), "Work Phone");
    appendOnUpdate(sb, oldContact.getCellPhone(), newContact.getCellPhone(), "Cell Phone");

    gui.getTxtLastEventDetails().setText(sb.toString());
  }

  /**
   * Appends an appropriate {@link String} if an object differs from before or was null.
   *
   * @param bldr {@link StringBuilder} to append to
   * @param previous the previous object value
   * @param current the current object value
   * @param description the description to add
   */
  private void appendOnUpdate(StringBuilder bldr, Object previous, Object current, String description) {
    if (Base.equals(previous, current)) {
      return;
    }

    if (previous == null) {
      bldr.append("Added value for ").append(description).append(" of: ").append(current).append("\n");
    }
    else if (current == null) {
      bldr.append("Removed value ").append(previous).append(" from ").append(description).append("\n");
    }
    else {
      bldr.append(description).append(" changed from \"").append(previous instanceof Date
                  ? dateFormat.format(previous) : previous).append("\" to \"").append(current instanceof Date
                    ? dateFormat.format(current) : current).append("\"\n");
    }
  }

  /**
   * Display the {@link Contact} in the frame.
   *
   * @param contact the {@link Contact} to display
   */
  private void displayContactDetails(Contact contact) {
  
    gui.getTxtLastName().setText(toString(contact.getLastName()));
    gui.getTxtFirstName().setText(toString(contact.getFirstName()));
    gui.getTxtHomeAddress().setText(toString(contact.getHomeAddress()));
    gui.getTxtWorkAddress().setText(toString(contact.getWorkAddress()));
    gui.getTxtBirthDate().setText(toString(contact.getBirthDate(), dateFormat));
    gui.getTxtAge().setText(toString(contact.getAge()));
    gui.getTxtPhoneNumbers().setText(toString(contact.getAllPhoneNumbers()));
    gui.getTxtEventCount().setText(toString(gui.getEventCount()));

  }

  /**
   * Helper method to format and display the output.
   *
   * @param value {@link Object} to display
   *
   * @return the {@link String} representation or a blank string
   */
  private static final String toString(Object value) {
    return toString(value, null);
  }

  /**
   * Helper method to format and display the output.
   *
   * @param value {@link Object} to display
   * @param formatter {@link Formatter} to format the display
   *
   * @return he {@link String} representation or a blank string
   */
  private static final String toString(Object value, Format formatter) {
    return value == null ? "" : formatter == null ? value.toString() : formatter.format(value);
  }

  /**
   * a default date formatter.
   */
  private static SimpleDateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");

  /*
   * The GUI screen object.
   */
  private ContactListenerGUI gui;
}
