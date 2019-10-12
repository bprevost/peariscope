#!/usr/bin/env python3

import sys
import time
import logging
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
logging.basicConfig()

NetworkTables.initialize(server='192.168.1.21')
nt = NetworkTables.getTable("Peariscope")
time.sleep(1)

for param in sys.argv[1:]:
    print(param, nt.getNumber(param, "N/A"))