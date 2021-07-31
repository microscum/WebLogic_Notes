// ------------------------------------------------------------------------
// -- DISCLAIMER:
// --    This code is provided for educational purposes only. It is NOT
// --    supported by Oracle World Wide Technical Support.
// --    The code has been tested and appears to work as intended.
// --    You should always run new code on a test instance initially.
// ------------------------------------------------------------------------

package com.example.ejb;

import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.ejb.Remove;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;

@MessageDriven(
		activationConfig = {
				@ActivationConfigProperty(
						propertyName = "destinationType", propertyValue = "javax.jms.Queue"),
				@ActivationConfigProperty(
						propertyName = "destinationJndiName", propertyValue = "jms.example.Queue2"),
				@ActivationConfigProperty(
						propertyName = "connectionFactoryJndiName", propertyValue = "jms.example.Factory1"),
				@ActivationConfigProperty(
						propertyName = "providerURL", propertyValue = "t3://host01:7011,host02:7012"),
		}
)
public class BasicQueueConsumerBean2 implements MessageListener {

	protected FileWriter writer;
	
    public BasicQueueConsumerBean2() {
    }
	
    public void onMessage(Message message) {
    	TextMessage textm = (TextMessage)message;
    	DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
        
    	// Wait a random amount of time to simulate message processing
    	int sleepTime = new Random().nextInt(700);
    	try {
			Thread.sleep(300 + sleepTime);
		} catch (InterruptedException e1) {
			e1.printStackTrace();
		}
    	
    	try {
        	writer = new FileWriter("BasicQueueConsumerBean2.log",true);
        	writer.write("Received message at " + dateFormat.format(new Date()) + " with contents[" + textm.getText() + "]\n");
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (JMSException e) {
			e.printStackTrace();
		}
    }
    
    @Remove
    public void remove() {
    }

}
