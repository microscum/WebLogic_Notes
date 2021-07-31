<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Memory Exhaustion Application</title>
</head>
<body>
        <h1>Memory Exhaustion Application</h1>
        <p> This application detects the amount of free memory available in the JVM and allocates an amount 
        of memory close to the full amount of memory available to force the WebLogic server to go into an 
        OVERLOADED state.
        <FORM NAME="data" METHOD="POST" Action="/SaturateMemory/MemoryServlet">

            Number of threads to run: <INPUT TYPE="TEXT"   NAME="numberOfThreads" VALUE="3"><br/>
            Seconds to run    : <INPUT TYPE="TEXT"   NAME="seconds" VALUE="10"><br/>
            <p/>
            <INPUT TYPE="SUBMIT" NAME="go" VALUE="submit">
        </FORM>
</body>
</html>