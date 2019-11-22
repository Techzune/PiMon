import os
from threading import Thread
from time import sleep

import serial

PORT_NAME = "/dev/ttyACM0"


def serialReader(portName, logFileName):
    port = serial.Serial(portName, 115200)
    logFile = open(logFileName, "a+")
    while True:
        readSerial = port.readline().decode('utf-8')
        logFile.writelines(readSerial)
        logFile.flush()

        logFile = limitFileSize(logFile)

        sleep(0.05)


def triggerSensorData(portName):
    port = serial.Serial(portName, 115200)
    command = "get sensors"
    command = command.encode()
    while True:
        port.write(command)
        sleep(0.2)


def limitFileSize(logFile, sizeLimit=32768):  # 32 KB
    logFileName = logFile.name
    if os.path.getsize(logFileName) >= sizeLimit:
        logFile.close()
        os.replace(logFileName, logFileName + ".old")
        logFile = open(logFileName, "a+")
    return logFile


def setupSerialHandlers(logFileName):
    Thread(target=serialReader, args=(PORT_NAME, logFileName), daemon=True).start()
    # Process(target=serialReader, args=(PORT_NAME,logFileName), daemon=True).start()
    # Thread(target=triggerSensorData, args=(PORT_NAME,), daemon=True).start()
    triggerSensorData(PORT_NAME)
