package com.oracle.wlsperf;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ejb.EJB;

import java.io.PrintWriter;
import java.util.Date;

/**
 * Servlet implementation class StuckServlet
 */
@WebServlet(description = "Servlet whch causes object proliferation and garbage collection", urlPatterns =
{ "/StressGCServlet" })
public class GCServlet extends HttpServlet
{
  private static final long serialVersionUID = 1L;
  @EJB
  private GCStressExecutor gse;

  /**
   * @see HttpServlet#HttpServlet()
   */
  public GCServlet()
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

    response.setContentType("text/html;charset=UTF-8");

    int numberOfThreads = Integer.parseInt(request
        .getParameter("numberOfThreads"));
    String seconds = request.getParameter("seconds");
    PrintWriter out = response.getWriter();
    try
    {

      out.println("<html>");
      out.println("<head>");
      out.println("<title>StressTestGC</title>");
      out.println("</head>");
      out.println("<body>");
      out.println("<h2>Servlet to cause object proliferation and garbage collection called... </h2>");
      // create and set a message to send
      out.println("<h4>Seconds to run: " + seconds + "</h4><br/>");
      out.println("<h4>Number of Threads: " + numberOfThreads + "</h4><br/>");

      int howMany = Integer.parseInt(seconds);
      for (int i = 0; i < numberOfThreads; i++)
      {
        out.println("Asynchronously calling EJB method generateGarbageCollectionActivity("
            + seconds + ") thread " + i + " at " + new Date()  + "</br>");
        gse.generateGarbageCollectionActivity(howMany);
        Thread.sleep(500);
      }    
      out.println("<br>");
      out.println("<a href=\"/StressGC/index.jsp\">Re-launch StressGC page</a>");
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
