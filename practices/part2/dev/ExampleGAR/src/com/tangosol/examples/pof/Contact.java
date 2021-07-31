
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.pof;

import com.tangosol.io.pof.PofReader;
import com.tangosol.io.pof.PofWriter;
import com.tangosol.io.pof.PortableObject;

import com.tangosol.util.Base;

import java.io.IOException;

import java.util.Date;

/**
 * Contact represents information needed to contact a person.
 * <p/>
 * The type implements PortableObject for efficient cross-platform
 * serialization.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author dag  2009.02.17
 * @author tam  2012.05.04 Refactored for use within Container examples
 */
public class Contact
        implements PortableObject {
  // ----- constructors ---------------------------------------------------

  /**
   * Default constructor (necessary for PortableObject implementation).
   */
  public Contact() {
  }

  /**
   * Construct a {@link Contact}.
   *
   * @param sFirstName      the first name
   * @param sLastName       the last name
   * @param addrHome        the home address
   * @param addrWork        the work address
   * @param homePhone       the home phone number 
   * @param workPhone       the work phone number 
   * @param cellPhone       the cell phone number 
   *                      
   * @param dtBirth         date of birth
   */
  public Contact(String sFirstName, String sLastName, Address addrHome, Address addrWork, PhoneNumber homePhone,
                 PhoneNumber workPhone, PhoneNumber cellPhone, Date dtBirth) {
    m_sFirstName = sFirstName;
    m_sLastName  = sLastName;
    m_addrHome   = addrHome;
    m_addrWork   = addrWork;
    m_homePhone  = homePhone;
    m_workPhone  = workPhone;
    m_cellPhone  = cellPhone;
    m_dtBirth    = dtBirth;
  }

  /**
   * Return the first name.
   *
   * @return the first name
   */
  public String getFirstName() {
    return m_sFirstName;
  }

  /**
   * Set the first name.
   *
   * @param sFirstName  the first name
   */
  public void setFirstName(String sFirstName) {
    m_sFirstName = sFirstName;
  }

  /**
   * Return the last name.
   *
   * @return the last name
   */
  public String getLastName() {
    return m_sLastName;
  }

  /**
   * Set the last name.
   *
   * @param sLastName  the last name
   */
  public void setLastName(String sLastName) {
    m_sLastName = sLastName;
  }

  /**
   * Return the home address.
   *
   * @return the home address
   */
  public Address getHomeAddress() {
    return m_addrHome;
  }

  /**
   * Set the home address.
   *
   * @param addrHome  the home address
   */
  public void setHomeAddress(Address addrHome) {
    m_addrHome = addrHome;
  }

  /**
   * Return the work address.
   *
   * @return the work address
   */
  public Address getWorkAddress() {
    return m_addrWork;
  }

  /**
   * Set the work address.
   *
   * @param addrWork  the work address
   */
  public void setWorkAddress(Address addrWork) {
    m_addrWork = addrWork;
  }

  /**
   * Get the date of birth.
   *
   * @return the date of birth
   */
  public Date getBirthDate() {
    return m_dtBirth;
  }

  /**
   * Set the date of birth.
   *
   * @param dtBirth  the date of birth
   */
  public void setBirthDate(Date dtBirth) {
    m_dtBirth = dtBirth;
  }

  /**
   * Get (approximate) age.
   *
   * @return age
   */
  public int getAge() {
    return (int) ((System.currentTimeMillis() - m_dtBirth.getTime()) / MILLIS_IN_YEAR);
  }

  /**
   * Get the home phone number.
   * 
   * @return the homePhone
   */
  public PhoneNumber getHomePhone() {
    return m_homePhone;
  }

  /**
   * Set the phone phone number.
   *
   * @param homePhone the m_homePhone to set
   */
  public void setHomePhone(PhoneNumber homePhone) {
    this.m_homePhone = homePhone;
  }

  /**
   * Get the work phone number.
   * 
   * @return the work phone number
   */
  public PhoneNumber getWorkPhone() {
    return m_workPhone;
  }

  /**
   * Set the work phone number.
   *
   * @param m_workPhone the m_workPhone to set
   */
  public void setWorkPhone(PhoneNumber workPhone) {
    this.m_workPhone = workPhone;
  }

  /**
   * Get the cell phone number.
   * 
   * @return the Cell Phone number
   */
  public PhoneNumber getCellPhone() {
    return m_cellPhone;
  }

  /**
   * Set the cell phone number.
   *
   * @param m_cellPhone the m_cellPhone to set
   */
  public void setCellPhone(PhoneNumber cellPhone) {
    this.m_cellPhone = cellPhone;
  }

  /**
   * Get all phone numbers for display purpose.
   */
  public String getAllPhoneNumbers() {
    StringBuilder sb = new StringBuilder();

    if (getHomePhone() != null) {
      sb.append("Home: ").append(getHomePhone()).append(" ");
    }

    if (getWorkPhone() != null) {
      sb.append("Work: ").append(getWorkPhone()).append(" ");
    }

    if (getCellPhone() != null) {
      sb.append("Cell: ").append(getCellPhone()).append(" ");
    }

    return sb.toString();
  }

  /**
   * {@inheritDoc}
   */
  public void readExternal(PofReader reader)
          throws IOException {
    m_sFirstName = reader.readString(FIRSTNAME);
    m_sLastName  = reader.readString(LASTNAME);
    m_addrHome   = (Address) reader.readObject(HOME_ADDRESS);
    m_addrWork   = (Address) reader.readObject(WORK_ADDRESS);
    m_homePhone  = (PhoneNumber) reader.readObject(HOME_PHONE);
    m_workPhone  = (PhoneNumber) reader.readObject(WORK_PHONE);
    m_cellPhone  = (PhoneNumber) reader.readObject(CELL_PHONE);
    m_dtBirth    = reader.readDate(BIRTH_DATE);
  }

  /**
  * {@inheritDoc}
  */
  public void writeExternal(PofWriter writer)
          throws IOException {
    writer.writeString(FIRSTNAME, m_sFirstName);
    writer.writeString(LASTNAME, m_sLastName);
    writer.writeObject(HOME_ADDRESS, m_addrHome);
    writer.writeObject(WORK_ADDRESS, m_addrWork);
    writer.writeObject(HOME_PHONE, m_homePhone);
    writer.writeObject(WORK_PHONE, m_workPhone);
    writer.writeObject(CELL_PHONE, m_cellPhone);
    writer.writeDate(BIRTH_DATE, m_dtBirth);

  }

  /**
  * {@inheritDoc}
  */
  public String toString() {
    StringBuilder sb =
      new StringBuilder(getFirstName()).append(" ").append(getLastName()).append("\nAddresses").append("\nHome: ")
        .append(getHomeAddress()).append("\nWork: ").append(getWorkAddress()).append("\nHome Phone: ")
        .append(getHomePhone()).append("\nWork Phone: ").append(getWorkPhone()).append("\nCell Phone: ")
        .append(getCellPhone());

    return sb.append("\nBirth Date: ").append(getBirthDate()).toString();
  }

  /**
   * Returns the hashCode of this {@link Contact}.
   *
   * @return the hashCode of this {@link Contact}
   */
  @Override
  public int hashCode() {
    final int prime  = 31;
    int       result = 1;

    result = prime * result + ((m_addrHome == null) ? 0 : m_addrHome.hashCode());
    result = prime * result + ((m_addrWork == null) ? 0 : m_addrWork.hashCode());
    result = prime * result + ((m_cellPhone == null) ? 0 : m_cellPhone.hashCode());
    result = prime * result + ((m_dtBirth == null) ? 0 : m_dtBirth.hashCode());
    result = prime * result + ((m_homePhone == null) ? 0 : m_homePhone.hashCode());
    result = prime * result + ((m_sFirstName == null) ? 0 : m_sFirstName.hashCode());
    result = prime * result + ((m_sLastName == null) ? 0 : m_sLastName.hashCode());
    result = prime * result + ((m_workPhone == null) ? 0 : m_workPhone.hashCode());

    return result;
  }

  /**
   * Compares this {@link Contact} with another.
   *
   * @param obj {@link Contact} to compare to
   *
   * @return if the contacts are equal
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }

    if (obj == null) {
      return false;
    }

    Contact that = (Contact) obj;

    return Base.equals(that.getHomeAddress(), getHomeAddress()) && Base.equals(that.getWorkAddress(), getWorkAddress())
           && Base.equals(that.getCellPhone(), getCellPhone())  && Base.equals(that.getBirthDate(), getBirthDate())
           && Base.equals(that.getHomePhone(), getHomePhone())  && Base.equals(that.getFirstName(), getFirstName())
           && Base.equals(that.getLastName(), getLastName())    && Base.equals(that.getWorkPhone(), getWorkPhone());
  }

  /**
   * The POF index for the FirstName property.
   */
  public static final int FIRSTNAME = 0;

  /**
   * The POF index for the LastName property.
   */
  public static final int LASTNAME = 1;

  /**
   * The POF index for the HomeAddress property.
   */
  public static final int HOME_ADDRESS = 2;

  /**
   * The POF index for the WorkAddress property.
   */
  public static final int WORK_ADDRESS = 3;

  /**
   * The POF index for the homePhone property.
   */
  public static final int HOME_PHONE = 4;

  /**
   * The POF index for the workPhone property.
   */
  public static final int WORK_PHONE = 5;

  /**
   * The POF index for the cellPhone property.
   */
  public static final int CELL_PHONE = 6;

  /**
   * The POF index for the BirthDate property.
   */
  public static final int BIRTH_DATE = 7;

  /**
   * Approximate number of millis in a year ignoring things such as leap
   * years. Suitable for example use only.
   */
  public static final long MILLIS_IN_YEAR = 1000L * 60L * 60L * 24L * 365L;

  /**
   * First name.
   */
  private String m_sFirstName;

  /**
   * Last name.
   */
  private String m_sLastName;

  /**
   * Home address.
   */
  private Address m_addrHome;

  /**
   * Work address.
   */
  private Address m_addrWork;

  /**
   * Birth Date.
   */
  private Date m_dtBirth;

  /**
   * Home phone.
   */
  private PhoneNumber m_homePhone;

  /**
   * Work phone.
   */
  private PhoneNumber m_workPhone;

  /**
   * Cell phone.
   */
  private PhoneNumber m_cellPhone;
}
