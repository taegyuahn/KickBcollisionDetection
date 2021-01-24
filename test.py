import random
import time
import json
from huskylib import HuskyLensLibrary

hl = HuskyLensLibrary("I2C","", address=0x32)

print(hl.learnedObjCount())