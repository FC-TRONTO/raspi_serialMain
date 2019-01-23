# coding: UTF-8

import serial
import time

def receiveDataLoop(shmem):
    # USBポートを使い、シリアル通信開始
    ev3_serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
    print(ev3_serial.portstr)
    while 1:
        read_data = ev3_serial.readline()
        # 読み込んだ文字列を,区切りでリストに変換
        sensorValues = read_data.strip().split(",")
        # 共有メモリの値を更新
        shmem.irAngle = int(sensorValues[0])
        shmem.uSonicDis = float(sensorValues[1])
        # 100msごとに実行
        time.sleep(0.1)

def target(shmem):
    receiveDataLoop(shmem)

def close():
    pass
