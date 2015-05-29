__author__ = 'cafacan'

import puka


class LogProducer:
    def __init__(self, host):
        self.producer = puka.Client(host)
        # connect sending party
        self.send_promise = self.producer.connect()
        self.producer.wait(self.send_promise)

        # declare queue (queue must exist before it is being used - otherwise messages sent to that queue will be discarded)
        self.send_promise = self.producer.queue_declare(queue='rabbit')
        self.producer.wait(self.send_promise)


    def send(self, message):
        while True:
            # send message to the queue named rabbit
            send_promise = self.producer.basic_publish(exchange='', routing_key='rabbit', body=message)
            self.producer.wait(send_promise)

            print "Message sent!"
            break

