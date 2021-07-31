
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.servlets;

import java.io.Serializable;

public class shoppingCartItem implements Serializable
{
	private static final long serialVersionUID = 1L;

	String name;
	String price;

	public void setName(String input)
	{
		name = input;
	}

	public void setPrice(String input)
	{
		price = input;
	}

	public String getPrice()
	{
		return price;
	}

	public String getName()
	{
		return name;
	}

}