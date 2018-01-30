import time
import math

from networktables import NetworkTables

table = NetworkTables.getTable('SmartDashboard')

t = time.time()
while time.time()-t < math.pi*2:
    dt = time.time()-t
    table.putNumber("sin_time", math.sin(dt))
    table.putNumber("cos_time", math.cos(dt))
    table.putNumber("time", time.time())
    table.putBoolean('log', True)
    time.sleep(1/20)

table.putBoolean('log', False)
NetworkTables.flush()
