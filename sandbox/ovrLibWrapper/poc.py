# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 10:13:56 2014

@author: Sam
"""
from ctypes import *
import time

dll_path = "C:/Development/ar_nerve/oculus/OculusSDK/Samples/OculusRoomTiny/Bin/Win/VS2013/Debug/Win32/OculusRoomTiny.dll"

#  load it
mydll = cdll.LoadLibrary(dll_path)

# Init the oculus
initRet = mydll.Init()
print initRet

#Get the configuration
deviceDesc = mydll.GetOculusInformation()

roll = c_double(0)
yaw = c_double(0)
pitch = c_double(0)

for i in range(1, 100000):
    mydll.GetOrientationParts(byref(roll), byref(yaw), byref(pitch))
    print("Left Eye = {0}, {1}, {2}".format(-roll.value * 180.0 / 3.14159, -yaw.value * 180.0 / 3.14159, pitch.value * 180.0 / 3.14159))
    time.sleep(0.01)

mydll.Release()