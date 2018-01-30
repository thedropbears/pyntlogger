import time
import math

from networktables import NetworkTables

table = NetworkTables.getTable('SmartDashboard')
log_entry = table.getEntry('log')
log_entry.setBoolean(True)

sin_time_entry = table.getEntry('sin_time')
cos_time_entry = table.getEntry('cos_time')
time_entry = table.getEntry('time')

t = time.time()
now = time.time()
while now - t < math.tau:
    dt = now - t
    sin_time_entry.setNumber(math.sin(dt))
    cos_time_entry.setNumber(math.cos(dt))
    time_entry.setNumber(now)
    time.sleep(1/20)
    now = time.time()

log_entry.setBoolean(False)
NetworkTables.flush()
