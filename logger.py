#!/usr/bin/env python3

import csv
import time

from networktables import NetworkTables


class NTLogger:

    def __init__(self):
        NetworkTables.startClientTeam(4774)
        self.table = NetworkTables.getTable('SmartDashboard')
        self.log_entry = self.table.getEntry('log')
        self.log_entry.setBoolean(False)
        self.logging = False
        self.entries = []
        self.logfile = None

    def start_logging(self):
        self.logging = True

        keys = [x for x in self.table.getKeys() if x != 'log']
        keys.sort()
        self.entries = [self.table.getEntry(key) for key in keys]

        fname = str(int(time.time()))+".csv"
        self.logfile = open(fname, 'w')
        self.writer = csv.writer(self.logfile)
        self.writer.writerow(keys)

    def stop_logging(self):
        self.logging = False
        self.entries = []
        self.writer = None
        if self.logfile:
            self.logfile.close()
            self.logfile = None

    def write_table(self):
        values = [entry.get() for entry in self.entries]
        self.writer.writerow(values)
        self.logfile.flush()

    def loop(self):
        log = self.log_entry.getBoolean(False)
        if self.logging and not log:
            self.stop_logging()
        elif self.logging:
            self.write_table()
        elif log:
            self.start_logging()

if __name__ == "__main__":
    logger = NTLogger()
    while True:
        time.sleep(1/20)
        logger.loop()
