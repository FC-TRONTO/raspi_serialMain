# coding: UTF-8

import serial
import time

class SerialController:
    def __init__(self):
        # USBポートを使い、シリアル通信開始
        self.ev3_serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
        print(self.ev3_serial.portstr)
    
    def receiveDataLoop(self, shmem):
        while 1:
            read_data = self.ev3_serial.readline()
            # 読み込んだ文字列を,区切りでリストに変換
            sensorValues = read_data.strip().split(",")
            # 共有メモリの値を更新
            if(len(sensorValues) == 2):
                if(self.is_int(sensorValues[0])):
                    shmem.irAngle = int(sensorValues[0])
                if(self.is_float(sensorValues[1])):
                    shmem.uSonicDis = float(sensorValues[1])
                #print('irAngle =', shmem.irAngle)
                #print('uSonicDis =', shmem.uSonicDis)
            # 100msごとに実行
            time.sleep(0.1)
    
    def write(self, sendData):
        self.ev3_serial.write(sendData)
        print('write', sendData)

    def target(self, shmem):
        self.receiveDataLoop(shmem)

    def close():
        pass

    def is_float(self, num):
        try:
            float(num)
        except ValueError:
            return False
        else:
            return True

    def is_int(self, num):
        try:
            int(num)
        except ValueError:
            return False
        else:
            return True
