'''
Created on Sep 7, 2014

@author: gearsad
'''
import lcm

from user_update_t import user_update_t

class LCMUserHerderController():
    def __init__(self, userViewModel):
        
        self.__userViewModel = userViewModel
        
        self.lc = lcm.LCM()
        self.subscription = self.lc.subscribe("ARNerve_UserHerder_Updates", self.UpdateUsersHandler)

    def UpdateUsersHandler(self, channel, data):
        '''
        Get the updated user and add it to the viewmdel
        '''
        msg = user_update_t.decode(data)
        if(self.__userViewModel):
            self.__userViewModel.UpdateUser(msg)

    def Update(self):
        self.lc.handle()

    def Disconnect(self):
        self.lc.unsubscribe(self.subscription)
