'''
Created on Nov 23, 2014

@author: gearsad
'''
from scene import Terrain
from scene import Bot
from scene import Axes
from scene import User
from scene import RoverBot

from core import UserManager

from math import sin, cos


class SceneManager(object):
    '''
    A manager for all the objects in the scene (and their controllers).
    '''

    def __init__(self):
        '''
        Create the world.
        '''
        return
        
    def Attach(self, userManager, renderManager):
        '''
        Attach the managers to the SceneManager
        '''
        self.__renderManager = renderManager
        
        # Create the user manager
        self.__userManager = userManager
        
        # When attached, build the test scene
        self.BuildTestScene()
        
            
    def BuildTestScene(self):
        '''
        Build a test scene.
        '''
        #Build a test world
        terrain = Terrain.Terrain(self.__renderManager.renderers, 10)
        # Initialize a set of test bots

        numBots = 8
        self.bots = []
        for i in xrange(0, numBots):
            bot = Bot.Bot(self.__renderManager.renderers)
            # Put the bot in a cool location 
            location = [10 * cos(i / float(numBots) * 6.242), 0, 10 * sin(i / float(numBots) * 6.242)]
            bot.SetSceneObjectPosition(location)
            
            # Make them all look outward
            yRot = 90.0 - i / float(numBots) * 360.0
            bot.SetSceneObjectOrientation([0, yRot, 0])
            
            self.bots.append(bot)
    
#         axes = Axes.Axes(self.renderManager.renderers)
        
        rover = RoverBot.RoverBot(self.__renderManager.renderers, "Girr!")
        rover.SetSceneObjectPosition([0, 0, 2])
          