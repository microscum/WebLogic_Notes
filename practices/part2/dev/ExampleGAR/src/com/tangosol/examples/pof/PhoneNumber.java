
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

import java.io.IOException;

/**
 * PhoneNumber represents a sequence of numers used to call a telephone.
 * <p/>
 * An example that uses the full sequence of numbers is a call from the United
 * States to Beijing, China: 011 86 10 85001234.
 * <p/>
 * The type implements PortableObject for efficient cross-platform
 * serialization..
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 *
 * @author dag  2009.02.17
 * @author tam  2012.05.09 Modified to use Integer for JSF compatibility
 */
public class PhoneNumber
        implements PortableObject {
  /**
   * Default constructor (necessary for PortableObject implementation).
   */
  public PhoneNumber() {
  }

  /**
   * Construct a Phone.
   *
   * @param nAccessCode   the numbers used to access international or
   *                      non-local calls
   * @param nCountryCode  the numbers used to designate a country
   * @param nAreaCode     the numbers used to indicate a geographical region
   * @param lLocalNumber  the local numbers
   */
  public PhoneNumber(Integer nAccessCode, Integer nCountryCode, Integer nAreaCode, Integer lLocalNumber) {
    m_nAccessCode  = nAccessCode;
    m_nCountryCode = nCountryCode;
    m_nAreaCode    = nAreaCode;
    m_lLocalNumber = lLocalNumber;
  }

  /**
   * Return the access code.
   *
   * @return the access code
   */
  public Integer getAccessCode() {
    return m_nAccessCode;
  }

  /**
   * Set the numbers used to access international or non-local calls.
   *
   * @param nAccessCode  the access code numbers
   */
  public void setAccessCode(Integer nAccessCode) {
    m_nAccessCode = nAccessCode;
  }

  /**
   * Return the country code.
   *
   * @return the country code
   */
  public Integer getCountryCode() {
    return m_nCountryCode;
  }

  /**
   * Set the country code.
   *
   * @param nCountryCode  the country code
   */
  public void setCountryCode(Integer nCountryCode) {
    m_nCountryCode = nCountryCode;
  }

  /**
   * Return the area code.
   *
   * @return the area code
   */
  public Integer getAreaCode() {
    return m_nAreaCode;
  }

  /**
   * Set the numbers used indicate a geographic area within a country.
   *
   * @param nAreaCode  the area code
   */
  public void setAreaCode(Integer nAreaCode) {
    m_nAreaCode = nAreaCode;
  }

  /**
   * Return the local or subscriber number.
   *
   * @return the local or subscriber number
   */
  public Integer getLocalNumber() {
    return m_lLocalNumber;
  }

  /**
   * Set the local or subscriber number.
   *
   * @param lLocalNumbeer  the local or subscriber number
   */
  public void setLocalNumber(Integer lLocalNumbeer) {
    m_lLocalNumber = lLocalNumbeer;
  }

  /**
  * {@inheritDoc}
  */
  public void readExternal(PofReader reader)
          throws IOException {
    m_nAccessCode  = (Integer) reader.readObject(ACCESS_CODE);
    m_nCountryCode = (Integer) reader.readObject(COUNTRY_CODE);
    m_nAreaCode    = (Integer) reader.readObject(AREA_CODE);
    m_lLocalNumber = (Integer) reader.readObject(LOCAL_NUMBER);
  }

  /**
  * {@inheritDoc}
  */
  public void writeExternal(PofWriter writer)
          throws IOException {
    writer.writeObject(ACCESS_CODE, m_nAccessCode);
    writer.writeObject(COUNTRY_CODE, m_nCountryCode);
    writer.writeObject(AREA_CODE, m_nAreaCode);
    writer.writeObject(LOCAL_NUMBER, m_lLocalNumber);
  }

  /**
  * {@inheritDoc}
  */
  public String toString() {
    StringBuilder sb = new StringBuilder();

    return sb.append(getAccessCode() == null && getAreaCode() == null
                     ? ""
                     : "+").append(blankIfNull(getAccessCode())).append(" ").append(blankIfNull(
                       getCountryCode())).append(" ").append(blankIfNull(getAreaCode())).append(" ").append(blankIfNull(
                       getLocalNumber())).toString();
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public int hashCode() {
    final int prime  = 31;
    int       result = 1;

    result = prime * result + ((m_lLocalNumber == null) ? 0 : m_lLocalNumber.hashCode());
    result = prime * result + ((m_nAccessCode == null) ? 0 : m_nAccessCode.hashCode());
    result = prime * result + ((m_nAreaCode == null) ? 0 : m_nAreaCode.hashCode());
    result = prime * result + ((m_nCountryCode == null) ? 0 : m_nCountryCode.hashCode());

    return result;
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }

    if (obj == null) {
      return false;
    }

    if (getClass() != obj.getClass()) {
      return false;
    }

    PhoneNumber other = (PhoneNumber) obj;

    if (m_lLocalNumber == null) {
      if (other.m_lLocalNumber != null) {
        return false;
      }
    }
    else if (!m_lLocalNumber.equals(other.m_lLocalNumber)) {
      return false;
    }

    if (m_nAccessCode == null) {
      if (other.m_nAccessCode != null) {
        return false;
      }
    }
    else if (!m_nAccessCode.equals(other.m_nAccessCode)) {
      return false;
    }

    if (m_nAreaCode == null) {
      if (other.m_nAreaCode != null) {
        return false;
      }
    }
    else if (!m_nAreaCode.equals(other.m_nAreaCode)) {
      return false;
    }

    if (m_nCountryCode == null) {
      if (other.m_nCountryCode != null) {
        return false;
      }
    }
    else if (!m_nCountryCode.equals(other.m_nCountryCode)) {
      return false;
    }

    return true;
  }

  /**
   * Helper method for toString.
   *
   * @param iValue value to check
   * @return the value in toString() else if null a "" returned
   */
  private String blankIfNull(Integer iValue) {
    return (iValue == null) ? "" : iValue.toString();
  }

  // ----- constants -------------------------------------------------------

  /**
   * The POF index for the AccessCode property.
   */
  public static final int ACCESS_CODE = 0;

  /**
   * The POF index for the CountryCode property.
   */
  public static final int COUNTRY_CODE = 1;

  /**
   * The POF index for the AreaCode property.
   */
  public static final int AREA_CODE = 2;

  /**
   * The POF index for the LocalNumber property.
   */
  public static final int LOCAL_NUMBER = 3;

  /**
   * The numbers used to access international or non-local calls.
   */
  private Integer m_nAccessCode;

  /**
   * The numbers used to designate a country in international calls.
   */
  private Integer m_nCountryCode;

  /**
   * The numbers used indicate a geographic area within a country.
   */
  private Integer m_nAreaCode;

  /**
   * The local number.
   */
  private Integer m_lLocalNumber;
}
