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

public class GenericProducerClient {

	
	public static void main(String[] args) throws Exception {
		if (args.length != 7) {
			System.out.println("Usage: GenericProducerClient name url factory dest txEnabled numMessages sleepTime");
			return;
		}
		String name = args[0];
		String url = args[1];
		String factory = args[2];
		String dest = args[3];
		boolean txEnabled = Boolean.parseBoolean(args[4]);
		int numMessages = Integer.parseInt(args[5]);
		int sleepTime = Integer.parseInt(args[6]);
		
		boolean isQueue = true;
		if(dest.contains("Topic")) {
			isQueue = false;
		}
		
		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
		
		if(isQueue) {
			BasicQueueSender sender = new BasicQueueSender(name,url,factory,dest,txEnabled);
			sender.init();
	
			for(int i = 0;i < numMessages; i++) {
				String timestamp = dateFormat.format(new Date());
			
				System.out.print(timestamp + "  Sending message to " + dest + "...");
				sender.send("This is the message content from " + name);
				System.out.println("done.");
			
				Thread.sleep(sleepTime);
			}
			if(txEnabled) {
				System.out.println("Commiting transaction");
				sender.commit();
			}
			sender.cleanup();
		} else {
			BasicTopicPublisher publisher = new BasicTopicPublisher(name,url,factory,dest,txEnabled);
			publisher.init();
			
			for(int i = 0;i < numMessages; i++) {
				String timestamp = dateFormat.format(new Date());
			
				System.out.print(timestamp + "  Sending message to " + dest + "...");
				publisher.send("This is the message content from " + name);
				System.out.println("done.");
				
				Thread.sleep(sleepTime);
			}
			if(txEnabled) {
				System.out.println("Commiting transaction");
				publisher.commit();
			}
			publisher.cleanup();
		}
	}
	
}
