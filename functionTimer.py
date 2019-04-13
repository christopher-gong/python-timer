import csv
import sys
import os
import time

class FunctionTimer:
    def __init__(self):
        self.info = dict()
        self.curr = dict()

    def begin(self, fn):
        self.curr[fn] = time.time()

    def end(self, fn):
        cfn = self.curr[fn]
        ifn = self.info.get(fn)
        count = 0
        t = 0
        if (ifn != None):
            t = ifn[0]
            count = ifn[1]
        self.info[fn] = [t + time.time() - cfn, count + 1]

    def revealInfo(self, loc):
        with open(loc, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["function", "total time", "times called", "avg time per call"])
            for key, val in self.info.items():
                writer.writerow([key] + val + [val[0] / val[1]])

    def clear(self):
        self.info = dict()
        self.curr = dict()