// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This code is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The code has been tested and appears to work as intended.
// --    You should always run new code on a test instance initially.
// ------------------------------------------------------------------------


package com.example.jms;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Hashtable;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class BasicQueueSender {

	public final static String JNDI_FACTORY="weblogic.jndi.WLInitialContextFactory";
	public final static String DEFAULT_CON_FACTORY_JNDI="weblogic.jms.XAConnectionFactory";
	
	protected String name;
    protected String url;
    protected String conFactoryJNDI;
    protected String queueJNDI;
    protected boolean txEnabled;

    protected Context ctx;
    protected QueueConnectionFactory qconFactory;
    protected QueueConnection qcon;
    protected QueueSession qsession;
    protected QueueSender qsender;
    protected Queue queue;
  
	public BasicQueueSender(String name, String url, String queueJNDI) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = DEFAULT_CON_FACTORY_JNDI;
		this.queueJNDI = queueJNDI;
		this.txEnabled = false;
	}

	public BasicQueueSender(String name, String url, String conFactoryJNDI,
			String queueJNDI, boolean txEnabled) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = conFactoryJNDI;
		this.queueJNDI = queueJNDI;
		this.txEnabled = txEnabled;
	}

    public String getName() {
      return name;
    }

    public InitialContext getInitialContext() throws NamingException {
      Hashtable<String,String> env = new Hashtable<String,String>();
      env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
      env.put(Context.PROVIDER_URL, url);
      return new InitialContext(env);
    }

    public void init() throws NamingException, JMSException {
      ctx = getInitialContext();
      qconFactory = (QueueConnectionFactory) ctx.lookup(conFactoryJNDI);
      qcon = qconFactory.createQueueConnection();
      qsession = qcon.createQueueSession(txEnabled, Session.AUTO_ACKNOWLEDGE);
      queue = (Queue) ctx.lookup(queueJNDI);
      qsender = qsession.createSender(queue);
    }

    public void send(String text) throws JMSException {
      TextMessage msg = qsession.createTextMessage(text);
      qsender.send(msg);
    }
    
    public void send() throws JMSException {
    	DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
    	String timestamp = dateFormat.format(new Date());
    	send("Message from " + name + " sent at " + timestamp);
    }
    
    public void commit() throws JMSException {
    	qsession.commit();
    }
    
    public void rollback() throws JMSException {
    	qsession.rollback();
    }

    public void cleanup() throws JMSException {
      qsender.close();
      qsession.close();
      qcon.close();
    }
	
}
