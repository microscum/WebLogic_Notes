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
import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class BasicQueueReceiver implements ExceptionListener, MessageListener {
	public final static String JNDI_FACTORY = "weblogic.jndi.WLInitialContextFactory";
	public final static String DEFAULT_CON_FACTORY_JNDI = "weblogic.jms.XAConnectionFactory";

	protected String name;
	protected String url;
	protected String conFactoryJNDI;
	protected String queueJNDI;
	protected boolean autoAck;
	protected int sleepTime;

	protected Context ctx;
	protected QueueConnectionFactory qconFactory;
	protected QueueConnection qcon;
	protected QueueSession qsession;
	protected QueueReceiver qreceiver;
	protected Queue queue;

	public BasicQueueReceiver(String name, String url, String queueJNDI) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = DEFAULT_CON_FACTORY_JNDI;
		this.queueJNDI = queueJNDI;
		this.autoAck = true;
		this.sleepTime = 3000;
	}

	public BasicQueueReceiver(String name, String url, String conFactoryJNDI,
			String queueJNDI, boolean autoAck, int sleepTime) {
		this.name = name;
		this.url = url;
		this.conFactoryJNDI = conFactoryJNDI;
		this.queueJNDI = queueJNDI;
		this.autoAck = autoAck;
		this.sleepTime = sleepTime;
	}

	public InitialContext getInitialContext() throws NamingException {
		Hashtable<String, String> env = new Hashtable<String, String>();
		env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
		env.put(Context.PROVIDER_URL, url);
		return new InitialContext(env);
	}

	public void init() throws NamingException, JMSException {
		ctx = getInitialContext();
		qconFactory = (QueueConnectionFactory) ctx.lookup(conFactoryJNDI);
		qcon = qconFactory.createQueueConnection();
		qcon.setExceptionListener(this);
		qcon.setClientID(name);
		if (autoAck) {
			qsession = qcon.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
		} else {
			qsession = qcon.createQueueSession(false,
					Session.CLIENT_ACKNOWLEDGE);
		}
		queue = (Queue) ctx.lookup(queueJNDI);
		qreceiver = qsession.createReceiver(queue);
		qreceiver.setMessageListener(this);
		qcon.start();
		System.out.println("Message Receiver connected to " + queueJNDI);
	}

	public void cleanup() throws JMSException {
		qreceiver.close();
		qsession.close();
		qcon.close();
	}

	public void onException(JMSException jmse) {
		System.out.println(jmse);
		System.out.println("");
		System.out
				.println("Receiver encountered an error. Will attempt to reconnect in 10 seconds.");
		try {
			Thread.sleep(10000);
			cleanup();
			init();
		} catch (Exception ex) {
			System.out.println(ex);
			System.exit(1);
		}
	}

	public void onMessage(Message msg) {
		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
		String timestamp = dateFormat.format(new Date());
		try {
			String msgText = ((TextMessage) msg).getText();
			System.out.println(timestamp + "  Message Received: [" + msgText
					+ "]");
			Thread.sleep(sleepTime);
			if (!autoAck) {
				msg.acknowledge();
				System.out.println("Message acknowledged");
			}
		} catch (Exception ex) {
			System.out.println(ex);
		}
	}

}
