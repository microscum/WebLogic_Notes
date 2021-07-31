package com.oracle.wlsperf;

import javax.ejb.LocalBean;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Random;
import java.util.logging.Logger;
import java.util.logging.Level;

/**
 * Session Bean implementation class StuckTreadsExecutor
 */
@Stateless
@LocalBean
public class BatchUpdatesExecutor
{
  private static final char[] symbols = new char[36];
  private static final Logger LOG = Logger.getLogger(BatchUpdatesExecutor.class
      .getName());
  static
  {
    for (int idx = 0; idx < 10; ++idx)
      symbols[idx] = (char) ('0' + idx);
    for (int idx = 10; idx < 36; ++idx)
      symbols[idx] = (char) ('a' + idx - 10);
  }
  private final char[] buf;
  private Random random = null;
  private DataSource myDB;

  /**
   * Default constructor.
   */
  public BatchUpdatesExecutor()
  {
    buf = new char[4000];
    random = new Random(System.currentTimeMillis());
    try
    {
      Context ctx = new InitialContext();
      this.myDB = (DataSource) ctx.lookup("jdbc/BatchUpd");

    }
    catch (NamingException e)
    {
      LOG.log(Level.SEVERE, e.getMessage());
    }

  }

  private String nextString()
  {
    for (int idx = 0; idx < buf.length; ++idx)
      buf[idx] = symbols[random.nextInt(symbols.length)];
    return new String(buf);
  }

  private boolean isTablePresent() throws Exception
  {
    boolean tablePresent = false;
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    conn = this.myDB.getConnection();
    stmt = conn.createStatement();
    rs = stmt
        .executeQuery("SELECT COUNT(*) FROM USER_TABLES WHERE TABLE_NAME = 'TEST_BATCH_UPD'");
    rs.next();
    int howMany = rs.getInt(1);
    if (howMany > 0)
    {
      tablePresent = true;
    }
    else
    {
      tablePresent = false;
    }
    try
    {
      rs.close();
      stmt.close();
      conn.close();
    }
    catch (SQLException ignore)
    {

    }

    return tablePresent;
  }

  private void createBatchTable() throws Exception
  {
    boolean isTableCreated = this.isTablePresent();
    if (!isTableCreated)
    {
      Connection conn = null;
      Statement stmt = null;

      conn = this.myDB.getConnection();
      stmt = conn.createStatement();
      stmt.execute("CREATE TABLE TEST_BATCH_UPD ( STMT_ID NUMBER NOT NULL, FIELD_1 VARCHAR2(4000), FIELD_2 VARCHAR2(4000), FIELD_3 VARCHAR2(4000))");

      try
      {
        stmt.close();
        conn.close();
      }
      catch (SQLException ignore)
      {
      }
    }
    else
    {
      Connection conn = null;
      Statement stmt = null;

      conn = this.myDB.getConnection();
      stmt = conn.createStatement();
      stmt.execute("TRUNCATE TABLE TEST_BATCH_UPD");

      try
      {
        stmt.close();
        conn.close();
      }
      catch (SQLException ignore)
      {
      }
    }

    return;
  }

  @SuppressWarnings("unused")
  @TransactionAttribute(TransactionAttributeType.REQUIRED)
  public void generateBatchUpdates(int loop, DataSource ds) throws Exception
  {
    this.myDB = ds;
    this.createBatchTable();
    Connection conn = null;
    PreparedStatement pstmt = null;

    conn = this.myDB.getConnection();
    conn.setAutoCommit(false);
    pstmt = conn
        .prepareStatement("INSERT INTO TEST_BATCH_UPD (STMT_ID,FIELD_1,FIELD_2,FIELD_3) VALUES (?,?,?,?)");
    for (int ii = 0; ii < loop; ii++)
    {
      pstmt.setInt(1, ii);
      pstmt.setString(2, this.nextString());
      pstmt.setString(3, this.nextString());
      pstmt.setString(4, this.nextString());
      pstmt.addBatch();
    }
    int[] updateCounts = pstmt.executeBatch();

    try
    {
      conn.commit();
      pstmt.close();
      conn.close();
    }
    catch (SQLException ignore)
    {

    }

  }

  @TransactionAttribute(TransactionAttributeType.REQUIRED)
  public void generateSimpleUpdates(int loop, DataSource ds) throws Exception
  {
    this.myDB = ds;
    this.createBatchTable();
    Connection conn = null;
    PreparedStatement pstmt = null;

    conn = this.myDB.getConnection();
    conn.setAutoCommit(true);
    pstmt = conn
        .prepareStatement("INSERT INTO TEST_BATCH_UPD (STMT_ID,FIELD_1,FIELD_2,FIELD_3) VALUES (?,?,?,?)");
    for (int ii = 0; ii < loop; ii++)
    {
      pstmt.setInt(1, ii);
      pstmt.setString(2, this.nextString());
      pstmt.setString(3, this.nextString());
      pstmt.setString(4, this.nextString());
      pstmt.executeUpdate();
    }

    try
    {
      conn.commit();
      pstmt.close();
      conn.close();
    }
    catch (SQLException ignore)
    {

    }
  }

}
