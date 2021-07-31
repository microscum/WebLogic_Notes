
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.tangosol.examples.contacts;

import com.tangosol.examples.pof.Address;
import com.tangosol.examples.pof.Contact;
import com.tangosol.examples.pof.PhoneNumber;

import com.tangosol.util.Base;

import java.sql.Date;

import java.util.Random;

/**
 *
 * DataGenerator generates random Contact information and store the result in a
 * CSV file. The data can may then be loaded with the LoaderExample.
 *
 * @author Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
 * 
 * @author dag  2009.02.19
 * @author tam  2012.05.13
 */
public class DataGenerator {

  /**
   * Return a random name.
   *
   * @return a random name
   */
  private static String getRandomName() {
    Random rand = Base.getRandom();
    int    cCh  = 4 + rand.nextInt(7);
    char[] ach  = new char[cCh];

    ach[0] = (char) ('A' + rand.nextInt(26));

    for (int of = 1; of < cCh; ++of) {
      ach[of] = (char) ('a' + rand.nextInt(26));
    }

    return new String(ach);
  }

  /**
   * Return a random phone number.
   * <p/>
   * The phone number contains including access, country, area code, and local
   * number.
   *
   * @return a random phone number
   */
  private static int[] getRandomPhoneDigits() {
    Random rand = Base.getRandom();

    return new int[] {
      11,                      // access code
      rand.nextInt(99),        // country code
      rand.nextInt(999),       // area code
      rand.nextInt(9999999)    // local number
    };
  }

  /**
   * Return a random Phone.
   *
   * @return a random phone
   */
  private static PhoneNumber getRandomPhone() {
    int[] anPhone = getRandomPhoneDigits();

    return new PhoneNumber(Integer.valueOf(anPhone[0]), Integer.valueOf(anPhone[1]), Integer.valueOf(anPhone[2]),
                           Integer.valueOf(anPhone[3]));
  }

  /**
   * Return a random Zip code.
   *
   * @return a random Zip code
   */
  private static String getRandomZip() {
    return Base.toDecString(Base.getRandom().nextInt(99999), 5);
  }

  /**
   * Return a random state.
   *
   * @return a random state
   */
  private static String getRandomState() {
    return STATE_CODES[Base.getRandom().nextInt(STATE_CODES.length)];
  }

  /**
   * Return a random date in millis before or after the epoch.
   *
   * @return a random date in millis before or after the epoch
   */
  public static long getRandomDateInMillis() {
    return (Base.getRandom().nextInt(40) - 20) * Contact.MILLIS_IN_YEAR;
  }

  /**
   * Generate a Contact with random information.
   *
   * @return a Contact with random information
   */
  public static Contact generateContact() {
    return new Contact("John", getRandomName(),
                       new Address("1500 Boylston St.", "", getRandomName(), getRandomState(), getRandomZip(), "US"),
                       new Address("8 Yawkey Way", "", getRandomName(), getRandomState(), getRandomZip(), "US"), null,
                       getRandomPhone(), null, new Date(getRandomDateInMillis()));
  }

  // ----- constants ------------------------------------------------------

  /**
   * US Postal Service two letter postal codes.
   */
  private static final String[] STATE_CODES = {
    "AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "OF", "DC", "FM", "FL", "GA", "GU", "HI", "ID", "IL", "IN",
    "IA", "KS", "KY", "LA", "ME", "MH", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
    "NC", "ND", "MP", "OH", "OK", "OR", "PW", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA",
    "WV", "WI", "WY"
  };
}
