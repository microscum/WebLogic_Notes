package com.example.jms;

import javax.jms.JMSException;
import javax.naming.NamingException;

import weblogic.jms.extensions.WLMessageProducer;

public class DelayedQueueSender extends BasicQueueSender {

	protected int timeToDeliver;
	
	public DelayedQueueSender(String name, String url, String queueJNDI, int timeToDeliver) {
		super(name, url, queueJNDI);
		this.timeToDeliver = timeToDeliver;
	}
	
	public DelayedQueueSender(String name, String url, String conFactoryJNDI,
			String queueJNDI, boolean txEnabled, int timeToDeliver) {
		super(name, url, conFactoryJNDI, queueJNDI, txEnabled);
		this.timeToDeliver = timeToDeliver;
	}
	
	public void init() throws NamingException, JMSException {
		super.init();
		WLMessageProducer wlproducer = (WLMessageProducer)qsender;
		wlproducer.setTimeToDeliver(timeToDeliver);
	}

}
