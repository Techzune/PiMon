from datetime import datetime
from time import sleep
import os

def populateLogFileTester(logFileName):
    # output to file
    logFile = open(logFileName, 'a+')
    print("Begining tester to populate log file")

    while True:
        # print current time
        logFile.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logFile.write("\n")
        # flush to file
        logFile.flush()
        # sleep
        sleep(0.2)