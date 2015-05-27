#!/usr/bin/env python

import threading
import time, os
from os import walk
from tailorThread import tailorThread

exitFlag = 0


class tailor ():

    def __init__(self):
        self.threads = []
        self.threadID = 1
        self.logFiles = []
        self.environmentPath = ''

    def kill(self):   
        for trd in self.threads:
            trd.kill()    

    def run(self):
               
        # Find log files
        for (dirpath, dirnames, filenames) in walk('./log-files/'):
            self.logFiles.extend(filenames)
            self.environmentPath = dirpath
            break

        # Create new threads
        for lfile in self.logFiles:
            print lfile
            thread = tailorThread(self.threadID, self.environmentPath+lfile)
            thread.daemon=True
            thread.start()
            self.threads.append(thread)
            self.threadID += 1

tail = tailor();
tail.run();

while True:
    time.sleep(2)
