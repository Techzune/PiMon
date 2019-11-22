from multiprocessing import Queue
from threading import Thread
from time import sleep

import serial

PORT_NAME = "/dev/ttyACM0"

if 'q' not in globals():
    q = Queue()


def serialReader(portName, logFileName):
    global q
    port = serial.Serial(portName, 115200)
    while True:
        readSerial = port.readline().decode('utf-8')
        q.put(readSerial)
        sleep(0.05)


def triggerSensorData(portName):
    port = serial.Serial(portName, 115200)
    command = "get sensors"
    command = command.encode()
    while True:
        port.write(command)
        sleep(0.2)


def setupSerialHandlers(logFileName):
    Thread(target=serialReader, args=(PORT_NAME, logFileName), daemon=True).start()
    # Process(target=serialReader, args=(PORT_NAME,logFileName), daemon=True).start()
    # Thread(target=triggerSensorData, args=(PORT_NAME,), daemon=True).start()
    triggerSensorData(PORT_NAME)
