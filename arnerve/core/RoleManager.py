'''
Created on Nov 30, 2014

@author: gearsad
'''

class RoleManager(object):
    '''
    The overall controller for the possible roles in the environment.
    '''


    def __init__(self):
        '''
        Create the roles structure.
        '''
        
        self.__roles = []
        
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
        print "Requesting the UserHerder to make this ARNerve client an observer"
        
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
        print "Requesting the UserHerder to make this ARNerve client a pilot"                        