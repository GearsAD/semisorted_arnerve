'''
Created on Aug 5, 2014

@author: gearsad
'''
# To allow the project to be run from outside Eclipse PyDev
import sys
sys.path.append('../')

import vtk
from math import cos, sin

from scene import Terrain
from scene import Bot
from scene import Axes
from scene import LIDAR

if __name__ == '__main__':
    
    # A renderer and render window
    renderers = []
    renderers.append(vtk.vtkRenderer())
    renderers.append(vtk.vtkRenderer())
    renderWindow = vtk.vtkRenderWindow()
    for renderer in renderers:
        renderWindow.AddRenderer(renderer)
    renderers[0].SetViewport(0, 0, 0.5, 1)
    renderers[1].SetViewport(0.5, 0, 1, 1)
    
    # Make it a little bigger than default
    renderWindow.SetSize(1920, 1080)
     
    # An interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    
    i = 0
    for renderer in renderers:
        camera = renderer.GetActiveCamera()
        camera.SetFocalPoint((0, 0, 0))
        camera.SetPosition((45, 20, -0.03+0.6*float(i)))
        i = i + 1
        
    # Create our new scene objects...
    terrain = Terrain.Terrain(renderers, 30)
    # Initialize a set of test bots
    numBots = 8
    bots = []
    for i in xrange(0, numBots):
        bot = Bot.Bot(renderers)
        # Put the bot in a cool location 
        location = [10 * cos(i / float(numBots) * 6.242), 0, 10 * sin(i / float(numBots) * 6.242)]
        bot.SetPositionVec3(location)
        
        # Make them all look outward
        yRot = 90.0 - i / float(numBots) * 360.0
        bot.SetOrientationVec3([0, yRot, 0])
        
        bots.append(bot)

    #axes = Axes.Axes(renderers)
        
    # Render an image (lights and cameras are created automatically)
    renderWindow.Render()

    # Begin mouse interaction
    renderWindowInteractor.Start()
    renderWindowInteractor.Initialize()
    
    pass
