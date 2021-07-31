package com.oracle.wlsperf;

import java.io.IOException;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;
import javax.ejb.EJB;
import java.io.PrintWriter;



/**
 * Servlet implementation class StuckServlet
 */
@WebServlet(description = "Servlet which tests batch updates", urlPatterns =
{ "/BatchUpdatesServlet" })
public class BatchUpdatesServlet extends HttpServlet
{
  private static final long serialVersionUID = 1L;
  @EJB
  private BatchUpdatesExecutor bue;

  /**
   * @see HttpServlet#HttpServlet()
   */
  public BatchUpdatesServlet()
  {
    super();
  }

  /**
   * @see Servlet#getServletInfo()
   */
  public String getServletInfo()
  {
    return null;
  }

  /**
   * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
   *      response)
   */
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException
  {
    processRequest(request, response);
  }

  /**
   * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
   *      response)
   */
  protected void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException
  {
    processRequest(request, response);
  }

  protected void processRequest(HttpServletRequest request,
      HttpServletResponse response) throws ServletException, IOException
  {
    DataSource myDB = null;
    response.setContentType("text/html;charset=UTF-8");

    int iterations = Integer.parseInt(request
        .getParameter("iterations"));
    String updType = request.getParameter("updtype");


    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head>");
    out.println("<title>Batch Updates Test</title>");
    out.println("</head>");
    out.println("<body>");
    try
    {
      Context ctx = new InitialContext();
      myDB = (DataSource) ctx.lookup("jdbc/BatchUpd");

    }
    catch (NamingException e)
    {
       e.printStackTrace(out);
    }
    try
    {


      if(updType.equals("Batch"))
      {
        out.println("<h2>Batch Updates requested...</h2>");
      }
      else
      {
        out.println("<h2>Sequence of Single Updates requested...</h2>");
      }
      long before = System.currentTimeMillis();
      if(updType.equals("Batch"))
      {
        try
        {
          bue.generateBatchUpdates(iterations,myDB);
          
        }
        catch(Exception e)
        {
          out.println("Method generateBatchUpdates triggered Exception");
          e.printStackTrace(out);
        }
      }
      else if(updType.equals("Simple"))
      {
        try
        {
          bue.generateSimpleUpdates(iterations,myDB);
        }
        catch(Exception e)
        {
          out.println("Method generateSimpleUpdates triggered Exception");
          e.printStackTrace(out);
        }
      }
      long after = System.currentTimeMillis();
      long howMany = after - before;
      if(updType.equals("Batch"))
      {
        out.println("<h4>Batch Updates. Inserted : "
          + iterations + " statements in "+howMany+" milliseconds</h4>");
      }
      else
      {
        out.println("<h4>Sequence of Single Updates. Inserted : "
            + iterations + " statements in "+howMany+" milliseconds</h4>");
      }
      out.println("<br>");

      out.println("<a href=\"/BatchUpdates/index.jsp\">Re-launch BatchUpdates page</a>");
      out.println("</body>");
      out.println("</html>");
    }

    catch (Exception exc)
    {
      System.out.println(exc.toString());
    }
    finally
    {
      out.close();
    }
  }

}
