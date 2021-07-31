<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Testing Batch Updates</title>
</head>
<body>
        <h1>Batch Update Application</h1>
        <p> This application allows you to submit the same INSERT statement in two different manners: either as a sequence of single inserts or as a batch of inserts. When the INSERT is batched the performance should improve significantly.  The table below highligths the different approaches:
		<table border="1">
  <tr>
    <th>Sequence of Single Updates</th>
    <th>Batch Updates</th>
  </tr>
  <tr>
    <td> <pre>conn = this.myDB.getConnection();
pstmt = conn.prepareStatement(&quot;INSERT INTO TEST_BATCH_UPD&quot;+<br> (STMT_ID, FIELD_1,FIELD_2,FIELD_3) VALUES (?,?,?,?)&quot;);
for(int ii = 0; ii < loop; ii++)
{
    pstmt.setInt(1, ii);
    pstmt.setString(2, &quot;&lt;Randomized String&gt;&quot;);
    pstmt.setString(3, &quot;&lt;Randomized String&gt;&quot;);
    pstmt.setString(4, &quot;&lt;Randomized String&gt;&quot;);
    pstmt.executeUpdate();
}</pre></td>
    <td><pre>conn = this.myDB.getConnection();
conn.setAutoCommit(false);
pstmt = conn.prepareStatement(&quot;INSERT INTO TEST_BATCH_UPD&quot;+<br> (STMT_ID,FIELD_1,FIELD_2,FIELD_3) VALUES (?,?,?,?)&quot;);
for(int ii = 0; ii < loop ; ii++)
{
   pstmt.setInt(1, ii);
   pstmt.setString(2, &quot;&lt;Randomized String&gt;&quot;);
   pstmt.setString(3, &quot;&lt;Randomized String&gt;&quot;);
   pstmt.setString(4, &quot;&lt;Randomized String&gt;&quot;);
   pstmt.addBatch();
}
int[] updateCounts = pstmt.executeBatch(); 
conn.commit();</pre></td><br>
  </tr>
</table>
<p>Note that in the batch update version, the connection does not commit the changes to the database after each statement. 
A commit statement must be explicitely issued at the end of the batch updates.
        <br><FORM NAME="data" METHOD="POST" Action="/BatchUpdates/BatchUpdatesServlet">
            Type of update: <INPUT TYPE="radio" name="updtype" value="Batch">Batch Update  
                            <INPUT TYPE="radio" name="updtype" value="Simple" checked>Single Update<br/>
            # of Statements: <INPUT TYPE="TEXT"   NAME="iterations" VALUE="1000"><br/>
            <p/>
            <INPUT TYPE="SUBMIT" NAME="go" VALUE="submit">
        </FORM>
</body>
</html>