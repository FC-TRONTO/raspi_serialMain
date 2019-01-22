# coding: UTF-8

import serial
import time

def receiveDataLoop(shmem):
    ev3_serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
    print(ev3_serial.portstr)
    count = 0
    while 1:
        read_data = ev3_serial.readline()
        print(read_data)
        print(shmem.irAngle)
        print(shmem.uSonicDis)
        shmem.irAngle = count
        count += 1
        time.sleep(2)

def target(shmem):
    receiveDataLoop(shmem)

def close():
    pass
