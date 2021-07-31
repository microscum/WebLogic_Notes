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
import java.util.Random;

import javax.jms.Message;
import javax.jms.TextMessage;

public class BuggyQueueReceiver extends BasicQueueReceiver {

	public BuggyQueueReceiver(String name, String url, String queueJNDI) {
		super(name, url, queueJNDI);
	}

	public BuggyQueueReceiver(String name, String url, String conFactoryJNDI,
			String queueJNDI, boolean autoAck, int sleepTime) {
		super(name, url, conFactoryJNDI, queueJNDI, autoAck, sleepTime);
	}
	
	public void onMessage(Message msg) {
		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
		String timestamp = dateFormat.format(new Date());
		try {
			String msgText = ((TextMessage) msg).getText();
			System.out.println(timestamp + "  Message Received: [" + msgText
					+ "]");
			Thread.sleep(sleepTime);
			
			if (new Random().nextInt(10) > 7) {
				qcon.close();
				Thread.sleep(sleepTime);
				init();
			} else if (!autoAck) {
				msg.acknowledge();
				System.out.println("Message acknowledged");
			}
		} catch (Exception ex) {
			System.out.println(ex);
		}
	}

}
