<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Stress GC Application</title>
</head>
<body>
        <h1>Stress GC Application</h1>
        <p> This application produces a large amount of objects which are created, stored into a collection, and subsequently cleared 
        from the collection in a loop. The intense object creation and destruction activity is meant to provoke frequent and long garbage collections.
        <FORM NAME="data" METHOD="POST" Action="/StressGC/StressGCServlet">

            Number of threads to run: <INPUT TYPE="TEXT"   NAME="numberOfThreads" VALUE="3"><br/>
            Seconds to run    : <INPUT TYPE="TEXT"   NAME="seconds" VALUE="10"><br/>
            <p/>
            <INPUT TYPE="SUBMIT" NAME="go" VALUE="submit">
        </FORM>
</body>
</html>