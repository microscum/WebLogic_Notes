
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.container.gui;

import com.tangosol.examples.container.gui.maplistener.ContactMapListener;
import com.tangosol.examples.pof.Contact;

import com.tangosol.net.CacheFactory;
import com.tangosol.net.NamedCache;

import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.Toolkit;

import java.util.concurrent.atomic.AtomicInteger;

import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

/**
 * Display a simple GUI screen to show any inserts, updates or deletes to a
 * {@link Contact} within a Coherence cache.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author tam  2012.05.20
 */
public class ContactListenerGUI {
  /**
   * Construct a new {@link ContactListenerGUI} and creates all required text fields.
   *
   */
  public ContactListenerGUI() {
    txtLastName         = new JTextField();
    txtFirstName        = new JTextField();
    txtHomeAddress      = new JTextField();
    txtWorkAddress      = new JTextField();

    txtBirthDate        = new JTextField();
    txtAge              = new JTextField();
    txtPhoneNumbers     = new JTextField();

    txtLastEvent        = new JTextField();
    txtEventCount       = new JTextField();

    txtLastEventDetails = new JTextArea(30, 80);
    scrollPane          = new JScrollPane(txtLastEventDetails);

    // ensure nothing can be changed
    txtLastName.setEditable(false);
    txtFirstName.setEditable(false);
    txtHomeAddress.setEditable(false);
    txtWorkAddress.setEditable(false);
    txtBirthDate.setEditable(false);
    txtAge.setEditable(false);
    txtPhoneNumbers.setEditable(false);
    txtLastEvent.setEditable(false);
    txtEventCount.setEditable(false);
    txtLastEventDetails.setEditable(false);

    eventCount = new AtomicInteger(0);
  }

  /**
   * Entry point for building the screen.
   */
  private void createAndShowGUI() {
    Dimension screenSize   = Toolkit.getDefaultToolkit().getScreenSize();
    int       height       = screenSize.height;
    int       width        = screenSize.width;
    int       windowWidth  = 800,
              windowHeight = 600;

    // Create and set up the window.
    frame = new JFrame("Coherence Container Extend Example");

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    frame.setSize(new Dimension(windowWidth, windowHeight));
    frame.setResizable(false);

    // Set up the content pane.
    addComponentsToPane(frame.getContentPane());

    // put the window in the middle of the screen
    frame.setLocation((width - windowWidth) / 2, (height - windowHeight) / 2);

    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
  }

  /**
   * Add all the components using null layout manager.
   *
   * @param pane pane to add to
   */
  private void addComponentsToPane(Container pane) {
    int startY = 70;

    pane.setLayout(null);

    JLabel txtHeader = new JLabel("Last Event from Contacts Cache");

    txtHeader.setBounds(new Rectangle(230, 10, 350, DEFAULT_HEIGHT + 10));
    txtHeader.setFont(new Font("Arial", Font.CENTER_BASELINE | Font.BOLD, 18));
    pane.add(txtHeader);

    addLine(pane, "Last Name:", 120, 200, startY, txtLastName);
    startY += (DEFAULT_HEIGHT + DEFAULT_SPACER);

    addLine(pane, "First Name:", 120, 200, startY, txtFirstName);
    startY += (DEFAULT_HEIGHT + DEFAULT_SPACER);

    addLine(pane, "Home Address:", 140, 450, startY, txtHomeAddress);
    startY += (DEFAULT_HEIGHT + DEFAULT_SPACER);

    addLine(pane, "Work Address:", 140, 450, startY, txtWorkAddress);
    startY += (DEFAULT_HEIGHT + DEFAULT_SPACER);

    addLine(pane, "Phone Numbers:", 140, 450, startY, txtPhoneNumbers);
    startY += (DEFAULT_HEIGHT + DEFAULT_SPACER);

    addLine(pane, "Birth Date:", 140, 100, startY, txtBirthDate);

    addLine(pane, "Age:", 50, 50, startY, 280, -185, txtAge);
    startY += (2 * (DEFAULT_HEIGHT + DEFAULT_SPACER));

    addLine(pane, "Last Event:", 140, 120, startY, txtLastEvent);
    addLine(pane, "Event Count:", 90, 50, startY, 280, -185, txtEventCount);

    startY += (2 * (DEFAULT_HEIGHT + DEFAULT_SPACER));

    addLine(pane, "Last Event Details:", 140, 520, startY, scrollPane);

    txtLastEvent.setText("Connecting...");

    txtLastEventDetails.setText("Connecting to Coherence Cluster via Coherence Extend...");
  }

  /**
   * Add a line consisting of a label and field.
   *
   * @param pane the {@link Container} to add to
   * @param sLabelDescription the label description
   * @param labelWidth width of the {@link JLabel} in pixels
   * @param fieldWidth width of the {@link JTextField} in pixels
   * @param startY current Y position
   * @param field the {@link JComponent} to add
   */
  private void addLine(Container pane, String sLabelDescription, int labelWidth, int fieldWidth, int startY,
                       JComponent field) {
    addLine(pane, sLabelDescription, labelWidth, fieldWidth, startY, 0 /* no offset */, DEFAULT_FIELD_GAP, field);
  }

  /**
   * Add a line consisting of a label and field and an additional offset for field positions.
   * This is used for items on the same line.
   *
   * @param pane the {@link Container} to add to
   * @param sLabelDescription the label description
   * @param labelWidth width of the {@link JLabel} in pixels
   * @param fieldWidth width of the {@link JTextField} in pixels
   * @param startY current Y position
   * @param startOffset the offset to add the label - for same line only
   * @param fieldOffset the offset between the label and field.
   * @param field the {@link JComponent} to add
   */
  private void addLine(Container pane, String sLabelDescription, int labelWidth, int fieldWidth, int startY,
                       int startOffset, int fieldOffset, JComponent field) {
    int    labelStartX = 50 + startOffset;
    int    fieldStartX = labelStartX + startOffset + (fieldOffset);

    JLabel label       = createLabel(sLabelDescription);

    label.setBounds(new Rectangle(labelStartX, startY, labelWidth, DEFAULT_HEIGHT));
    pane.add(label);

    // for the text area set the bounds according to the rows
    if (field instanceof JScrollPane) {
      field.setBounds(new Rectangle(fieldStartX, startY, fieldWidth, DEFAULT_HEIGHT * 10));
    }
    else if (field instanceof JTextField) {
      field.setBounds(new Rectangle(fieldStartX, startY, fieldWidth, DEFAULT_HEIGHT));
    }

    pane.add(field);
  }

  /**
   * Entry point to display GUI client.
   *
   * @param args standard array of {@link String} arguments
   */
  public static void main(String[] args) {
    ContactListenerGUI gui = new ContactListenerGUI();

    gui.createAndShowGUI();

    try {
      NamedCache cacheContacts = CacheFactory.getCache("contacts");

      cacheContacts.addMapListener(new ContactMapListener(gui));
     }
    catch (Exception e) {
      gui.getTxtLastEvent().setText("Error");
      gui.getTxtLastEventDetails().setText(e.getMessage());
     }

    gui.getTxtLastEvent().setText("Connected");
  }

  /**
   * Constructs a label.
   *
   * @param sLabelText the text for the label
   * @return the constructed label
   */
  private JLabel createLabel(String sLabelText) {
    JLabel label = new JLabel(sLabelText);

    label.setAlignmentX(Component.RIGHT_ALIGNMENT);

    return label;
  }

  /**
   * Get the lastName {@link JTextField}.
   *
   * @return the lastName {@link JTextField}
   */
  public JTextField getTxtLastName() {
    return txtLastName;
  }

  /**
   * Set the lastName {@link JTextField}.
   *
   * @param txtLastName {@link JTextField} to set value to
   */
  public void setTxtLastName(JTextField txtLastName) {
    this.txtLastName = txtLastName;
  }

  /**
   * Get the firstName {@link JTextField}.
   *
   * @return the firstName {@link JTextField}
   */
  public JTextField getTxtFirstName() {
    return txtFirstName;
  }

  /**
   * Set the firstName {@link JTextField}.
   *
   * @param txtFirstName {@link JTextField} to set value to
   */
  public void setTxtFirstName(JTextField txtFirstName) {
    this.txtFirstName = txtFirstName;
  }

  /**
   * Get the homeAddress {@link JTextField}.
   *
   * @return the homeAddress {@link JTextField}
   */
  public JTextField getTxtHomeAddress() {
    return txtHomeAddress;
  }

  /**
   * Set the homeAddress {@link JTextField}.
   *
   * @param txtHomeAddress {@link JTextField} to set value to
   */
  public void setTxtHomeAddress(JTextField txtHomeAddress) {
    this.txtHomeAddress = txtHomeAddress;
  }

  /**
   * Get the homeAddress {@link JTextField}.
   *
   * @return the homeAddress {@link JTextField}
   */
  public JTextField getTxtWorkAddress() {
    return txtWorkAddress;
  }

  /**
   * Set the firstName {@link JTextField}.
   *
   * @param txtWorkAddress {@link JTextField} to set value to
   */
  public void setTxtWorkAddress(JTextField txtWorkAddress) {
    this.txtWorkAddress = txtWorkAddress;
  }

  /**
   * Get the birthDate {@link JTextField}.
   *
   * @return the birthDate {@link JTextField}
   */
  public JTextField getTxtBirthDate() {
    return txtBirthDate;
  }

  /**
   * Set the birthDate {@link JTextField}.
   *
   * @param txtBirthDate {@link JTextField} to set value to
   */
  public void setTxtBirthDate(JTextField txtBirthDate) {
    this.txtBirthDate = txtBirthDate;
  }

  /**
   * Get the age {@link JTextField}.
   *
   * @return the age {@link JTextField}
   */
  public JTextField getTxtAge() {
    return txtAge;
  }

  /**
   * Set the age {@link JTextField}.
   *
   * @param txtAge the age {@link JTextField}
   */
  public void setTxtAge(JTextField txtAge) {
    this.txtAge = txtAge;
  }

  /**
   * Get the birthDate {@link JTextField}.
   *
   * @return the birthDate {@link JTextField}
   */
  public JTextField getTxtPhoneNumbers() {
    return txtPhoneNumbers;
  }

  /**
   * Set the phoneNumbers {@link JTextField}.
   *
   * @param txtPhoneNumbers {@link JTextField} to set value to
   */
  public void setTxtPhoneNumbers(JTextField txtPhoneNumbers) {
    this.txtPhoneNumbers = txtPhoneNumbers;
  }

  /**
   * Get the lastEvent {@link JTextField}.
   *
   * @return he lastEvent {@link JTextField}
   */
  public JTextField getTxtLastEvent() {
    return txtLastEvent;
  }

  /**
   * Set the lastEvent {@link JTextField}.
   *
   * @param txtLastEvent {@link JTextField} to set value to
   */
  public void setTxtLastEvent(JTextField txtLastEvent) {
    this.txtLastEvent = txtLastEvent;
  }

  /**
   * Get the eventCount {@link JTextField}.
   *
   * @return the eventCount {@link JTextField}
   */
  public JTextField getTxtEventCount() {
    return txtEventCount;
  }

  /**
   * Set the eventCount {@link JTextField}.
   *
   * @param txtEventCount {@link JTextField} to set value to
   */
  public void setTxtEventCount(JTextField txtEventCount) {
    this.txtEventCount = txtEventCount;
  }

  /**
   * Get the lastEventDetails {@link JTextField}.
   *
   * @return lastEventDetails {@link JTextField}
   */
  public JTextArea getTxtLastEventDetails() {
    return txtLastEventDetails;
  }

  /**
   * Set the evetnCount {@link JTextField}.
   *
   * @param txtLastEventDetails
   */
  public void setTxtLastEventDetails(JTextArea txtLastEventDetails) {
    this.txtLastEventDetails = txtLastEventDetails;
  }

  /**
   * Get the current event count.
   *
   * @return the current event count
   */
  public AtomicInteger getEventCount() {
    return eventCount;
  }

  /**
   * Set the current eventCount
   *
   * @param eventCount value to set to
   */
  public void setEventCount(AtomicInteger eventCount) {
    this.eventCount = eventCount;
  }

  /**
   * Get the current frame.
   *
   * @return the current frame
   */
  public JFrame getFrame() {
    return frame;
  }

  /**
   * Set the current frame.
   *
   * @param frame the frame to set
   */
  public void setFrame(JFrame frame) {
    this.frame = frame;
  }

  /**
   * Default height for each line.
   */
  private static final int DEFAULT_HEIGHT = 24;

  /**
   * Default spacer between lines.
   */
  private static final int DEFAULT_SPACER = 4;

  /**
   * Default gap between field and label.
   */
  private static final int DEFAULT_FIELD_GAP = 150;

  /**
   * Last name of the {@link Contact}.
   */
  private JTextField    txtLastName;
  
  /**
   * First name of the {@link Contact}.
   */
  private JTextField    txtFirstName;
  
  /**
   * Home address of the {@link Contact}.
   */
  private JTextField    txtHomeAddress;
  
  /**
   * Work address of the {@link Contact}.
   */
  private JTextField    txtWorkAddress;
  
  /**
   * Birth Date of the {@link Contact}.
   */
  private JTextField    txtBirthDate;
  
  /**
   * Age of the {@link Contact}.
   */
  private JTextField    txtAge;
  
  /** 
   * Phone numbers of the {@link Contact}.
   */
  private JTextField    txtPhoneNumbers;
  
  /**
   * Last event that occurred.
   */
  private JTextField    txtLastEvent;
  
  /**
   * Count of events.
   */
  private JTextField    txtEventCount;
  
  /**
   * Detail of the last event.
   */
  private JTextArea     txtLastEventDetails;
  
  /**
   * The scroll pane to contain the last event details.
   */
  private JScrollPane   scrollPane;
  
  /**
   * The main {@JFrame} used to render screen screen.
   */
  private JFrame        frame;
  
  /**
   * A counter of events.
   */
  private AtomicInteger eventCount;
}
