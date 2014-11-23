'''
Created on Sep 7, 2014

@author: gearsad
'''
import lcm

from head_tracking_info_t import head_tracking_info_t

class LCMController():
    def __init__(self):
        
        self.HeadTrackingOrientation = [0.0, 0.0, 0.0]
        
        self.lc = lcm.LCM()
        self.subscription = self.lc.subscribe("Pilot_J.Sparrow", self.Head_Tracking_Handler)

    def Head_Tracking_Handler(self, channel, data):
        msg = head_tracking_info_t.decode(data)
#         print("Received message on channel \"%s\"" % channel)
#         print(" timestamp = %s" % str(msg.timestamp))
#         print(" orientation = %s" % str(msg.orientation))
#         print("")
        #Update the head-tracking location
        self.HeadTrackingOrientation = msg.orientation

    def Update(self):
        self.lc.handle()

    def Disconnect(self):
        self.lc.unsubscribe(self.subscription)
