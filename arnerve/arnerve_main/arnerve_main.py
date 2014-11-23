'''
Created on Nov 20, 2014

@author: gearsad
'''

import sys

from core import RenderManager
from scene import MenuItem
from scene import MenuItemController

from math import cos, sin

from scene import Terrain
from scene import Bot
from scene import Axes
from scene import LIDAR

from scene import InteractorMapUser
from scene import Interactor1stPersonUser
from scene import Interactor3rdPerson

if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print "Run arneve with the following paramaters - name, type, width, height"
        sys.exit()
    
    name = sys.argv[1]
    device = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    
    #Initialize a rendering loop
    render = RenderManager.RenderManager(name, device, 1280, 720, False)
    
    render.Initialize()
    
    # Create our new scene objects...
    terrain = Terrain.Terrain(render.renderers, 100)
    # Initialize a set of test bots
    numBots = 8
    bots = []
    for i in xrange(0, numBots):
        bot = Bot.Bot(render.renderers)
        # Put the bot in a cool location 
        location = [10 * cos(i / float(numBots) * 6.242), 0, 10 * sin(i / float(numBots) * 6.242)]
        bot.SetPositionVec3(location)
        
        # Make them all look outward
        yRot = 90.0 - i / float(numBots) * 360.0
        bot.SetOrientationVec3([0, yRot, 0])
        
        bots.append(bot)

    axes = Axes.Axes(render.renderers)
    
    #Menu = MenuItemController.MenuItemController(render.renderers, render.renderWindowInteractor, "UserMenu")
    #Menu.BuildTestMenu()
    
    render.renderWindowInteractor.Start()
    
    pass