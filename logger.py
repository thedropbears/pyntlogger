import csv
import time

from networktables import NetworkTables

log_frequency = 50

class NTLogger:

    def __init__(self):
        NetworkTables.startClientTeam(4774)
        self.table = NetworkTables.getTable('SmartDashboard')
        self.table.putBoolean('log', False)
        self.logging = False
        self.keys = []
        self.logfile = None

    def start_logging(self):
        self.logging = True
        self.keys = sorted(self.table.getKeys())
        fname = str(int(time.time()))+".csv"
        self.logfile = open(fname, 'w')
        self.writer = csv.writer(self.logfile)
        self.writer.writerow(self.keys)
        self.logfile.flush()

    def stop_logging(self):
        self.logging = False
        self.keys = []
        self.writer = None
        if self.logfile:
            self.logfile.close()
            self.logfile = None

    def write_table(self):
        values = [self.table.getValue(key) for key in self.keys]
        self.writer.writerow(values)
        self.logfile.flush()

    def loop(self):
        log = self.table.getValue('log')
        if self.logging and not log:
            self.stop_logging()
        elif self.logging:
            self.write_table()
        elif log:
            self.start_logging()

if __name__ == "__main__":
    logger = NTLogger()
    last_tm = time.time()
    while True:
        try:
            # time.sleep((1/log_frequency) - (time.time()-last_tm))
            time.sleep(1/20)
        except ValueError as e:
            print(e)
        logger.loop()
        last_tm = time.time()
