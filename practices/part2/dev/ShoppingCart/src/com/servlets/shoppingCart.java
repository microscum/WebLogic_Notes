
// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This script is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The script has been tested and appears to work as intended.
// --    You should always run new scripts on a test instance initially.
// --
// ------------------------------------------------------------------------

package com.servlets;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.Vector;

public class shoppingCart extends HttpServlet
{
	private static final long serialVersionUID = 1L;

	@SuppressWarnings("unchecked")
	public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException
	{
		System.out.println("within shopping cart servlet");

		response.setContentType("text/html");
		ServletOutputStream out = response.getOutputStream();
		out.print("<HTML><HEAD><TITLE>Supply Categories</TITLE></HEAD>");
		out.print("<BODY><CENTER>");
		out.print("<table>");
		out.print("<tr><td><CENTER><b><h2>Shopping Cart Store</h2></b></CENTER></td>");
		out.print("</tr>");
		out.print("</table>");

		out.print("<FONT SIZE='4' COLOR='navy'>");

		HttpSession session = request.getSession(true);
		Vector<shoppingCartItem> scitems = (Vector<shoppingCartItem>) session.getAttribute("cart");
		String name = request.getParameter("item");
		String price = request.getParameter("price");

		shoppingCartItem newItem = new shoppingCartItem();
		newItem.setName(name);
		newItem.setPrice(price);

		if (scitems == null)
		{
			out.print("added new element<BR>" + name);
			System.out.println("added new element: " + name);
			scitems = new Vector<shoppingCartItem>();
			scitems.addElement(newItem);
			session.setAttribute("cart", scitems);

		} else {
			out.print("<BR>added new element<BR>" + name);
			System.out.println("added new element: " + name);
			scitems.addElement(newItem);
			session.setAttribute("cart", scitems);
		}

		out.print("</FONT>");
		out.print("<BR><A HREF='./welcome.jsp'>Back To Home Page</A><BR>");
		out.print("</BODY></HTML>");
	}
}