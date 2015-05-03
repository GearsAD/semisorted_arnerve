'''
Created on Nov 30, 2014

@author: gearsad
'''

import lcm

import role_request_t

class RoleManager(object):
    '''
    The overall controller for the possible roles in the environment.
    '''

    def __init__(self):
        '''
        Create the roles structure.
        '''
        self.__roles = []
    
    def Attach(self, userManager, lcmManager):
        '''
        Attach relevant objects to the RoleManager
        '''
        self.__userManager = userManager
        self.__lcmManager = lcmManager
    
    def GetMenuItemsRolesAndCallbacks(self):
        '''
        TODO - Complete [GearsAD]
        '''
        
        roles = [
                ['Observer', self.RequestAsObserver],
                ['Commander', self.RequestAsCommander],
                ['Planner', self.RequestAsPlanner],
                ['Pilot', self.RequestAsPilot]]
        return roles
    
    def RequestAsObserver(self, param):
        '''
        Request the UserHerder to make this user an observer, which will have a callback to set the respective interactor style.
        '''
        request = role_request_t.role_request_t()
        
        request.timestamp = 0
        request.userName = self.__userManager.GetCurrentUser()
        request.requestedRole = 0
        request.isUpdatingRole = 0
        request.newPlannerGroup = ""
        request.isUpdatingPlannerGroup = 0
        request.requestedBotNameToPilot = ""
        request.isUpdatingBot = 0
        
        self.__lcmManager.SendRoleRequest(request.encode())
        
    def RequestAsCommander(self, param):
        '''
        Request the UserHerder to make this user the commander, which will have a callback to set the respective interactor style.
        '''
        print "Requesting the UserHerder to make this ARNerve client a commander"
        
    def RequestAsPlanner(self, requestedGroupToPlan):
        '''
        Request the UserHerder to make this user a planner of a group, which will have a callback to set the respective interactor style.
        '''
        print "Requesting the UserHerder to make this ARNerve client a planner"

    def RequestAsPilot(self, requestedBotToPilot):
        '''
        Request the UserHerder to make this user a pilot of an available vechicle, which will have a callback to set the respective interactor style.
        '''
        request = role_request_t.role_request_t()
        
        request.timestamp = 0
        request.userName = self.__userManager.GetCurrentUser()
        request.requestedRole = 1
        request.isUpdatingRole = 0
        request.newPlannerGroup = ""
        request.isUpdatingPlannerGroup = 0
        request.requestedBotNameToPilot = requestedBotToPilot
        request.isUpdatingBot = 1
        
        self.__lcmManager.SendRoleRequest(request.encode())   
        
    def ParseRoleResponse(self, roleResponse):
        '''
        Parse a role response and update the pilots/planners if needed
        '''
        return                    