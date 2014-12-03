'''
Created on Nov 30, 2014

@author: gearsad
'''

class BotManager(object):
    '''
    The overall controller for all the bots in the environment.
    '''


    def __init__(self):
        '''
        Create the bots structure.
        '''
        
        self.__bots = []
        
    def GetMenuItemsBotsAndCallbacks(self):
        '''
        TODO - Complete [GearsAD]
        '''
        
        bots = [
                ['Rover1', None],
                ['UAV1', None],
                ['Gundam1', None],
                ['Atlas1', None],
                ['SPHERE1', None]]
        return bots