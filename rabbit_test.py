import puka
import time

consumer = puka.Client("amqp://localhost/")
# connect receiving party
receive_promise = consumer.connect()
consumer.wait(receive_promise)
# start waiting for messages, also those sent before (!), on the queue named rabbit
receive_promise = consumer.basic_consume(queue='rabbit', no_ack=True)

print "Starting receiving!"

while True:
	received_message = consumer.wait(receive_promise)
	print "GOT: %r" % (received_message['body'])
	time.sleep(1/2)
