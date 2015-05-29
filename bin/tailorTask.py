__author__ = 'cafacan'

import threading
import time
import os

import logPublisher


class TailorThread(threading.Thread):
    def __init__(self, thread_id, file_path):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.filePath = file_path
        self.logPublisher = logPublisher.LogProducer("amqp://guest:guest@192.168.57.252:5672/")

    def run(self):
        print "Starting " + self.filePath
        process_data("T" + str(self.threadID), self.filePath, self.logPublisher)
        print "Exiting " + self.filePath


def process_data(thread_name, file_path, publisher):
    # Set the filename and open the file
    log_file = open(file_path, 'r')

    # Find the size of the file and move to the end
    st_results = os.stat(file_path)
    st_size = st_results[6]
    log_file.seek(st_size)

    while True:
        where = log_file.tell()
        line = log_file.readline()
        if not line:
            time.sleep(.3)
            log_file.seek(where)
        else:
            if len(line) > 1:
                message = "%s : %s" % (thread_name, line)  # already has newline
                print message
                publisher.send(message)
                time.sleep(.3)

    publisher.close()

