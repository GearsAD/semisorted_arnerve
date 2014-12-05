'''
Created on Sep 7, 2014

@author: gearsad
'''
import lcm

#Import the user types
from user_update_t import user_update_t

#Import the bot types
from bot_update_t import bot_update_t
from bot_control_command_t import bot_control_command_t

#Import the role types
from role_response_t import role_response_t

class LCMManager():
    
    def __init__(self):
        
        #Broadcast across the wire
        self.lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
        self.__subscriptions = []
        self.__subscriptions.append(self.lc.subscribe("ARNerve_UserUpdates", self.UpdateUsersHandler))
        self.__subscriptions.append(self.lc.subscribe("ARNerve_UserHerder_RoleResponses", self.UpdateFromRoleResponse))
        
        # Add all the bot channels.
        self.__subscriptions.append(self.lc.subscribe("ARNerve_Bot_Update_GIRR", self.UpdateBot))

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
            
        #HACK TESTING...
#         botControl = bot_control_command_t()
#         botControl.name = "GIRR"
#         botControl.botTreadVelLeft = 0
#         botControl.botTreadVelLeft = 0
#         if msg.kinect.is_lhandclosed and msg.kinect.is_rhandclosed:
#             botControl.botTreadVelLeft = 1.0
#             botControl.botTreadVelright = 1.0
#         else:
#             if msg.kinect.is_lhandclosed:
#                 print "---Left Hand CLosed!"
#                 botControl.botTreadVelLeft = 1.0
#                 botControl.botTreadVelright = -1.0
#             if msg.kinect.is_rhandclosed:
#                 print "---Right Hand CLosed!"
#                 botControl.botTreadVelLeft = -1.0
#                 botControl.botTreadVelright = 1.0
#         botControl.isInfraredOn = 0
#         botControl.isLightsOn = 0
#         botControl.timestamp = 0
#         self.lc.publish("ARNerve_Bot_Control_GIRR", botControl.encode())
        
    
    def UpdateFromRoleResponse(self, channel, data):
        '''
        Get the role response, parse it, and send it to the role manager
        '''
        roleResponse = role_response_t.decode(data)
        
        # Now pass it to the role manager
        self.__roleManager.ParseRoleResponse(roleResponse)
        
    def UpdateBot(self, channel, data):
        '''
        Update from a bot frame
        '''
        botUpdate = bot_update_t.decode(data)
        print "[LCMManager] Got an update for bot {0}".format(botUpdate.name)
        return
          
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