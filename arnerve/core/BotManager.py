'''
Created on Nov 30, 2014

@author: gearsad
'''
from scene.RoverBot import RoverBot

class BotManager(object):
    '''
    The overall controller for all the bots in the environment.
    '''

    def __init__(self):
        '''
        Create the bots structure.
        '''
        
        self.__botsLCM = []
        self.__botModels = []

    def Attach(self, roleManager, renderManager, lcmManager):
        '''
        Attach the managers to the UserManager
        '''
        self.__renderManager = renderManager
        self.__roleManager = roleManager
        self.__lcmManager = lcmManager
        
    def Update(self):
        '''
        Update the bots
        '''
        return
        
    def UpdateBotFromLCM(self, updateBot):
        '''
        Method to update the bot list with a new or current bot.
        '''
        #Update the other users
        found = False
        index = 0
        for bot in self.__botsLCM:
            if(bot.name == updateBot.name): #Update this user
                self.__botsLCM[index] = updateBot #Replace the user, we found it
                self.__botModels[index].UpdateBotFromLCM(updateBot)
                found = True
            else:
                index = index + 1
        if(found is not True):
            newBot = RoverBot(self.__renderManager.renderers, updateBot.name)
            print "Adding another bot - moving him away from the axis! Remove in future."
            newBot.vtkActor.SetPosition([0, 0, 1])
            print "[BotManager.py] Ignoring the other user for now."
            self.__botsLCM.append(updateBot)
            self.__botModels.append(newBot)
        
    def GetMenuItemsBotsAndCallbacks(self):
        '''
        TODO - Complete [GearsAD]
        '''
        botNameCallbacks = []
        for bot in self.__botsLCM:
            newCallback = [bot.name, self.RequestBotControl, bot]
            botNameCallbacks.append(newCallback)
        return botNameCallbacks
    
    def RequestBotControl(self, lcmBot):
        '''
        Request the UserHerder to make this user a pilot of a specific bit, which will have a callback to set the respective interactor style when the response comes through.
        '''   
        print "Requesting control of bot {0}".format(lcmBot.name)
        return