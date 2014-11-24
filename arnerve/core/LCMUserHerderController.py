'''
Created on Sep 7, 2014

@author: gearsad
'''
import lcm

from user_update_t import user_update_t

class LCMUserHerderController():
    def __init__(self, userManager):
        
        self.__userManager = userManager
        
        self.lc = lcm.LCM()
        self.subscription = self.lc.subscribe("ARNerve_UserHerder_KineSource", self.UpdateUsersHandler)

    def UpdateUsersHandler(self, channel, data):
        '''
        Get the updated user and add it to the viewmdel
        '''
        msg = user_update_t.decode(data)
        if(self.__userManager):
            self.__userManager.UpdateUser(msg)
        print msg.kinect.istrackingbody
        if msg.kinect.istrackingbody == 1:
            i = 0
            
    def Update(self):
        self.lc.handle()

    def Disconnect(self):
        self.lc.unsubscribe(self.subscription)
