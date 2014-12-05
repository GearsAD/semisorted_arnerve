'''
Created on Sep 7, 2014

@author: gearsad
'''
import lcm

from user_update_t import user_update_t
import role_response_t

class LCMManager():
    
    def __init__(self):
        
        self.lc = lcm.LCM()
        self.__subscriptions = []
        self.__subscriptions.append(self.lc.subscribe("ARNerve_UserUpdates", self.UpdateUsersHandler))
        self.__subscriptions.append(self.lc.subscribe("ARNerve_UserHerder_RoleResponses", self.UpdateFromRoleResponse))

    def Attach(self, userManager, roleManager):
        '''
        Attach relevant objects to the RoleManager
        '''
        self.__userManager = userManager
        self.__roleManager = roleManager

    def UpdateUsersHandler(self, channel, data):
        '''
        Get the updated user and add it to the user manager
        '''
        msg = user_update_t.decode(data)
        if(self.__userManager):
            self.__userManager.UpdateUserFromLCM(msg)
    
    def UpdateFromRoleResponse(self, channel, data):
        '''
        Get the role response, parse it, and send it to the role manager
        '''
        roleResponse = role_response_t.decode(data)
        
        # Now pass it to the role manager
        self.__roleManager.ParseRoleResponse(roleResponse)
          
    def Update(self):
        self.lc.handle()

    def Disconnect(self):
        for subscription in self.__subscriptions:
            self.lc.unsubscribe(subscription)

    def SendRoleRequest(self, lcmRoleRequest):
        '''
        Send a role change request to the UserHerder
        '''
        self.lc.publish("ARNerve_UserHerder_RoleRequests", lcmRoleRequest)