__author__ = 'cafacan'

# !/usr/bin/env python

import os

from tailorTask import TailorThread


class Tailor():
    def __init__(self):
        self.threads = []
        self.threadID = 1
        self.logFiles = []
        self.environmentPath = ''

    def run(self):

        # Find log files
        for (dir_path, dir_names, file_names) in os.walk('./log-files/'):
            self.logFiles.extend(file_names)
            self.environmentPath = dir_path
            break

        # Create new threads
        for log_file in self.logFiles:
            print log_file
            thread = TailorThread(self.threadID, self.environmentPath + log_file)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
            self.threadID += 1




