import threading
import time, os
from log_producer import logProducer

exitFlag = 0
class tailorThread (threading.Thread):
    
    def __init__(self, threadID, filePath):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.filePath = filePath
        self.logPublisher = logProducer("amqp://localhost/")

    def run(self):
        print "Starting " + self.filePath
        process_data("T" + str(self.threadID), self.filePath, self.logPublisher)
        print "Exiting " + self.filePath

    def kill(self):
        exitFlag = 1

def process_data(threadName, filePath, publisher):
    while not exitFlag:
        #Set the filename and open the file
        file = open(filePath,'r')

        #Find the size of the file and move to the end
        st_results = os.stat(filePath)
        st_size = st_results[6]
        file.seek(st_size)

        while not exitFlag :
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                if len(line) > 1:
                    message = "%s : %s" % (threadName, line) # already has newline
                    print message
                    publisher.send(message)
                    time.sleep(1)
    
    publisher.close()
