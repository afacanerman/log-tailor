#!/usr/bin/env python

import Queue
import threading
import time, os
from os import walk

exitFlag = 0

class tailorThread (threading.Thread):
    
    def __init__(self, threadID, filePath):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.filePath = filePath

    def run(self):
        print "Starting " + self.filePath
        process_data("T" + str(self.threadID), self.filePath)
        print "Exiting " + self.filePath

def process_data(threadName, filePath):
    while not exitFlag:
        #Set the filename and open the file
        file = open(filePath,'r')

        #Find the size of the file and move to the end
        st_results = os.stat(filePath)
        st_size = st_results[6]
        file.seek(st_size)

        while 1:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                if len(line) > 1:
                    print "%s : %s" % (threadName, line) # already has newline
                    time.sleep(1/3)


threads = []
threadID = 1
logFiles = []
environmentPath = ''

# Find log files
for (dirpath, dirnames, filenames) in walk('c:\\logs\\'):
    logFiles.extend(filenames)
    environmentPath = dirpath
    break

# Create new threads
for lfile in logFiles:
    print lfile
    thread = tailorThread(threadID, environmentPath+lfile)
    thread.start()
    threads.append(thread)
    threadID += 1


