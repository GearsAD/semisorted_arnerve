'''
Created on Sep 7, 2014

@author: gearsad
'''
from ctypes import *
import time

class OculusController():
    def __init__(self):
        
        dll_path = "C:/Development/ar_nerve/oculus/OculusSDK/Samples/OculusRoomTiny/Bin/Win/VS2013/Debug/Win32/OculusRoomTiny.dll"

        #  load it
        self.mydll = cdll.LoadLibrary(dll_path)
        initRet = self.mydll.Init()
        print initRet
        
        self.HeadTrackingOrientation = [0, 0, 0]

    def Update(self):
        roll = c_double(0)
        yaw = c_double(0)
        pitch = c_double(0)

        self.mydll.GetOrientationParts(byref(roll), byref(yaw), byref(pitch))
        
        #print("Left Eye = {0}, {1}, {2}".format(-roll.value * 180.0 / 3.14159, -yaw.value * 180.0 / 3.14159, pitch.value * 180.0 / 3.14159))
        self.HeadTrackingOrientation = [roll.value * 180.0 / 3.14159, yaw.value * 180.0 / 3.14159, pitch.value * 180.0 / 3.14159]

    def Disconnect(self):
        self.mydll.Release()