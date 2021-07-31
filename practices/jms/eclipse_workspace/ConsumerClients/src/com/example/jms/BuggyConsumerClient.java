// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This code is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The code has been tested and appears to work as intended.
// --    You should always run new code on a test instance initially.
// ------------------------------------------------------------------------

package com.example.jms;

public class BuggyConsumerClient {

	public static void main(String[] args) throws Exception {
		if (args.length != 6) {
			System.out
					.println("Usage: BuggyConsumerClient name url factory dest autoAck sleepTime");
			return;
		}
		String name = args[0];
		String url = args[1];
		String factory = args[2];
		String dest = args[3];
		boolean autoAck = Boolean.parseBoolean(args[4]);
		int sleepTime = Integer.parseInt(args[5]);

		boolean isQueue = true;
		if (dest.contains("Topic")) {
			isQueue = false;
		}

		if (isQueue) {
			BasicQueueReceiver receiver = new BuggyQueueReceiver(name, url,
					factory, dest, autoAck, sleepTime);
			receiver.init();

			System.out.println("Receiver started. To exit, press Enter.");
			System.out.println();
			System.console().readLine();
			receiver.cleanup();
		} else {
			// to do
		}
		System.exit(1);
	}

}
