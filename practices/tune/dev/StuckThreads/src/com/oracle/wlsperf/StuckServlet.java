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
@WebServlet(description = "Servlet whch causes WebLogic Stuck Threads", urlPatterns =
{ "/StuckServlet" })
public class StuckServlet extends HttpServlet
{
  private static final long serialVersionUID = 1L;
  @EJB
  private StuckTreadsExecutor ste;

  /**
   * @see HttpServlet#HttpServlet()
   */
  public StuckServlet()
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
      out.println("<title>Servlet stuck</title>");
      out.println("</head>");
      out.println("<body>");
      out.println("<h1>Servlet to cause stuck threads called... </h1>");
      // create and set a message to send
      out.println("<h3>Seconds to run: " + seconds + "</h3><br/>");
      out.println("<h3>Number of Threads: " + numberOfThreads + "</h3><br/>");
      for (int i = 0; i < numberOfThreads; i++)
      {

        out.println("Asynchronously calling EJB method generateCpuLoad(" + seconds +") thread " + i + " at " + new Date() + "</br>");
        int howMany = Integer.parseInt(seconds);
        ste.generateCpuLoad(howMany);
        Thread.sleep(500);
      }
      out.println("<br>");
      out.println("<a href=\"/StuckThreads/index.jsp\">Re-launch</a>");
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
