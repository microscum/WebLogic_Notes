
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
import java.util.Enumeration;

public class browseCategories extends HttpServlet
{
	private static final long serialVersionUID = 1L;

	public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException
	{
		System.out.println("within browseCategories servlet");

		response.setContentType("text/html");
		ServletOutputStream out = response.getOutputStream();
		out.print("<HTML><HEAD><TITLE>Supply Categories</TITLE></HEAD>");
		out.print("<BODY><CENTER>");
		out.print("<table>");
		out.print("<tr><td><CENTER><b><h2>Shopping Cart Store</h2></b></CENTER></td>");
		out.print("</tr>");
		out.print("</table>");
		out.print("<FONT SIZE='4' COLOR='navy'>");

		Enumeration<String> e = request.getParameterNames();

		while (e.hasMoreElements())
		{
			String name = (String) e.nextElement();
			if (name.equals("boxWriting"))
				getWritingSupplies(out);
			if (name.equals("boxPaper"))
				getPaperSupplies(out);
			if (name.equals("boxFurniture"))
				getFurnitureSupplies(out);
		}
		
		out.print("</FONT>");
		out.print("<BR><A HREF='./welcome.jsp'>Back To Home Page</A><BR>");
		out.print("</BODY></HTML>");
	}

	public void getWritingSupplies(ServletOutputStream out) throws IOException
	{
		out.print("<TABLE WIDTH='75%' ALIGN='center' BGCOLOR='wheat'>");
		out.print("<TR><TD COLSPAN='2' ALIGN='center'>Writing Supplies</TD></TR>");
		out.print("<TR><TD ALIGN='right' WIDTH='50%'>box of 12 pens (black)</TD><TD ALIGN='left' WIDTH='50%'>&nbsp;&nbsp;&nbsp;4.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>box of 12 pens (blue)</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;4.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>box of 12 pens (red)</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;4.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>3 mechanical pencils</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;8.99</TD></TR>");
		out.print("</TABLE><BR><BR>");
	}

	public void getPaperSupplies(ServletOutputStream out) throws IOException
	{
		out.print("<TABLE WIDTH='75%' ALIGN='center' BGCOLOR='wheat'>");
		out.print("<TR><TD COLSPAN='2' ALIGN='center'>Paper Supplies</TD></TR>");
		out.print("<TR><TD ALIGN='right' WIDTH='50%'>package of 500 sheets multipurpose paper</TD><TD ALIGN='left' WIDTH='50%'>&nbsp;&nbsp;&nbsp;6.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>package of 5 legal pads</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;15.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>100 Post-It notes</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;7.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>1 subject notebook</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;2.99</TD></TR>");
		out.print("</TABLE><BR><BR>");
	}

	public void getFurnitureSupplies(ServletOutputStream out) throws IOException
	{
		out.print("<TABLE WIDTH='75%' ALIGN='center' BGCOLOR='wheat'>");
		out.print("<TR><TD COLSPAN='2' ALIGN='center'>Furniture Supplies</TD></TR>");
		out.print("<TR><TD ALIGN='right' WIDTH='50%'>corner computer desk</TD><TD ALIGN='left' WIDTH='50%'>&nbsp;&nbsp;&nbsp;199.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>adjustable chair</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;99.99</TD></TR>");
		out.print("<TR><TD ALIGN='right'>leather adjustable chair</TD><TD ALIGN='left'>&nbsp;&nbsp;&nbsp;139.99</TD></TR>");
		out.print("</TABLE><BR><BR>");
	}
}