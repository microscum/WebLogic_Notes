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
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.jms.Topic;
import javax.jms.TopicConnection;
import javax.jms.TopicConnectionFactory;
import javax.jms.TopicPublisher;
import javax.jms.TopicSession;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class BasicTopicPublisher {

	public final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
	public final static String DEFAULT_CON_FACTORY_JNDI = "weblogic.jms.XAConnectionFactory";

	protected String name;
	protected String url;
	protected String conFactoryJNDI;
	protected String topicJNDI;
	protected boolean txEnabled;

	protected Context ctx;
	protected TopicConnectionFactory tconFactory;
	protected TopicConnection tcon;
	protected TopicSession tsession;
	protected TopicPublisher tpublisher;
	protected Topic topic;

	public BasicTopicPublisher(String name, String url, String topicJNDI) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = DEFAULT_CON_FACTORY_JNDI;
		this.topicJNDI = topicJNDI;
		this.txEnabled = false;
	}

	public BasicTopicPublisher(String name, String url, String conFactoryJNDI,
			String topicJNDI, boolean txEnabled) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = conFactoryJNDI;
		this.topicJNDI = topicJNDI;
		this.txEnabled = txEnabled;
	}

	public String getName() {
		return name;
	}

	public InitialContext getInitialContext() throws NamingException {
		Hashtable<String, String> env = new Hashtable<String, String>();
		env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
		env.put(Context.PROVIDER_URL, url);
		return new InitialContext(env);
	}

	public void init() throws NamingException, JMSException {
		ctx = getInitialContext();
		tconFactory = (TopicConnectionFactory) ctx.lookup(conFactoryJNDI);
		tcon = tconFactory.createTopicConnection();
		tsession = tcon.createTopicSession(txEnabled, Session.AUTO_ACKNOWLEDGE);
		topic = (Topic) ctx.lookup(topicJNDI);
		tpublisher = tsession.createPublisher(topic);
	}

	public void send(String text) throws JMSException {
		TextMessage msg = tsession.createTextMessage(text);
		tpublisher.send(msg);
	}

	public void send() throws JMSException {
		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
		String timestamp = dateFormat.format(new Date());
		send("Message from " + name + " sent at " + timestamp);
	}
	
	public void commit() throws JMSException {
    	tsession.commit();
    }
    
    public void rollback() throws JMSException {
    	tsession.rollback();
    }

	public void cleanup() throws JMSException {
		tpublisher.close();
		tsession.close();
		tcon.close();
	}

}
