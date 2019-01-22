# coding: UTF-8

from multiprocessing import Process, Value
from ctypes import Structure, c_int, c_double
import os
import serialCom

# 共有メモリの構造体
class Point(Structure):
    _fields_ = [('irAngle', c_int), ('uSonicDis', c_double)]

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == '__main__':
    info('main line')
    # 共有メモリの準備
    shmem = Value(Point, 0)
    p_serialCom = Process(target=serialCom.target(shmem))
    p_serialCom.start()
    p_serialCom.join()

