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

public class DelayedProducerClient {

	public static void main(String[] args) throws Exception {
		if (args.length != 9) {
			System.out
					.println("Usage: DelayedProducerClient name url factory dest txEnabled numMessages sleepTime delayTime numDelayMessages");
			return;
		}
		String name = args[0];
		String url = args[1];
		String factory = args[2];
		String dest = args[3];
		boolean txEnabled = Boolean.parseBoolean(args[4]);
		int numMessages = Integer.parseInt(args[5]);
		int sleepTime = Integer.parseInt(args[6]);
		int delayTime = Integer.parseInt(args[7]);
		int numDelayMessages = Integer.parseInt(args[8]);

		if (dest.contains("Topic")) {
			System.out.println("This client only supports queues.");
			System.exit(1);
		}

		DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

		BasicQueueSender sender = new BasicQueueSender(name, url, factory,
				dest, txEnabled);
		sender.init();
		BasicQueueSender delaySender = new DelayedQueueSender(name, url, factory,
				dest, txEnabled, delayTime);
		delaySender.init();
		

		for (int i = 0; i < numMessages; i++) {
			String timestamp = dateFormat.format(new Date());

			System.out
					.print(timestamp + "  Sending message to " + dest + "...");
			if((i + 1) % (numMessages / numDelayMessages) == 0) {
				delaySender.send("This is the message content from " + name + "2");
			} else {
				sender.send("This is the message content from " + name + "1");
			}
			System.out.println("done.");

			Thread.sleep(sleepTime);
		}
		if (txEnabled) {
			System.out.println("Commiting transaction");
			sender.commit();
			delaySender.commit();
		}
		sender.cleanup();

	}

}
