package com.oracle.wlsperf;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ejb.EJB;

import java.io.PrintWriter;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Date;

/**
 * Servlet implementation class StuckServlet
 */
@WebServlet(description = "Servlet which causes WebLogic Overload State", urlPatterns =
{ "/MemoryServlet" })
public class MemoryServlet extends HttpServlet
{
  private static final long serialVersionUID = 1L;
  @EJB
  private MemoryExhaustionExecutor mee;

  /**
   * @see HttpServlet#HttpServlet()
   */
  public MemoryServlet()
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

  @SuppressWarnings("static-access")
  protected void processRequest(HttpServletRequest request,
      HttpServletResponse response) throws ServletException, IOException
  {

    response.setContentType("text/html;charset=UTF-8");

    int numberOfThreads = Integer.parseInt(request
        .getParameter("numberOfThreads"));
    String seconds = request.getParameter("seconds");
    long maxMem = Runtime.getRuntime().maxMemory();
    long totalMem = Runtime.getRuntime().totalMemory();
    long freeMem = Runtime.getRuntime().freeMemory();
    System.out.println("Current mem (long): " + freeMem);
    BigDecimal newVal = new BigDecimal(freeMem * 0.95);
    BigDecimal divisor = new BigDecimal(numberOfThreads);
    BigDecimal result = newVal.divide(divisor, 2, RoundingMode.HALF_UP);
    long eachMem = result.longValue();

    PrintWriter out = response.getWriter();
    try
    {

      out.println("<html>");
      out.println("<head>");
      out.println("<title>Memory Exhaustion</title>");
      out.println("</head>");
      out.println("<body>");
      out.println("<h2>Servlet to cause memory exhaustion called... </h2>");
      // create and set a message to send
      out.println("<h4>Seconds to run: " + seconds + "</h4><br/>");
      out.println("<h4>Number of Threads: " + numberOfThreads + "</h4><br/>");
      out.println("<h4>Total Memory available to the JVM (in MB): "
          + (totalMem / 1024 / 1024) + "</h4>");
      out.println("<h4>Maximum Memory available to the JVM (in MB): "
          + (maxMem / 1024 / 1024) + "</h4>");
      out.println("<h4>Memory available to the JVM (in MB): "
          + (freeMem / 1024 / 1024) + "</h4>");
      int howMany = Integer.parseInt(seconds);
      for (int i = 0; i < numberOfThreads; i++)
      {
        out.println("Asynchronously calling EJB method generateMemoryLoad("
            + (eachMem /1024 / 1024) + "," + seconds + ") thread " + i + " at " + new Date()
            + "</br>");

        mee.generateMemoryLoad(eachMem, howMany);
        Thread.sleep(500);
      }
      freeMem = Runtime.getRuntime().freeMemory();
      out.println("<h4>Memory now available to the JVM (in MB): "
          + (freeMem / 1024 / 1024) + "</h4>");

      newVal = new BigDecimal(freeMem * 0.95);
      long newmem = newVal.longValue();
      mee.generateMemoryLoad(newmem, howMany);
      Thread.currentThread().sleep(2000);
      freeMem = Runtime.getRuntime().freeMemory();
      out.println("<h4>Memory now available to the JVM: "
          + (freeMem / 1024 / 1024) + "</h4>");
      out.println("<br>");

      out.println("<a href=\"/SaturateMemory/index.jsp\">Re-launch SaturateMemory page</a>");
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
