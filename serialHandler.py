from multiprocessing import Queue
from threading import Thread
from time import sleep

import serial

PORT_NAME = "/dev/ttyACM0"


def serialReader(portName, queue):
    port = serial.Serial(portName, 115200)
    while True:
        readSerial = port.readline().decode('utf-8')
        queue.put(readSerial)
        sleep(0.05)


def triggerSensorData(portName):
    port = serial.Serial(portName, 115200)
    command = "get sensors"
    command = command.encode()
    while True:
        port.write(command)
        sleep(0.2)


def setupSerialHandlers(queue):
    Thread(target=serialReader, args=(PORT_NAME, queue), daemon=True).start()
    triggerSensorData(PORT_NAME)
