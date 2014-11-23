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

from scene import InteractorMapUser
from scene import Interactor1stPersonUser
from scene import Interactor3rdPerson
from scene import Interactor1stPersonVuzix

def __3DRenderingLoop(obj, event):
    '''
    Main loop for rendering at a constant ~30Hz
    '''
    iren = obj
    iren.GetRenderWindow().Render()
    
if __name__ == '__main__':
    renderWindow = vtk.vtkRenderWindow()
    
    # A renderer and render window
    renderers = []
    renderers.append(vtk.vtkRenderer())
    renderers.append(vtk.vtkRenderer())
    renderWindow = vtk.vtkRenderWindow()
    for renderer in renderers:
        renderWindow.AddRenderer(renderer)
    renderers[0].SetViewport(0, 0, 0.5, 1)
    renderers[1].SetViewport(0.5, 0, 1, 1)
    
    # Let's put in the other screen
    renderWindow.SetSize(1600, 1024)
#    renderWindow.SetPosition(1600,0)
     
    # An interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    
    # Create our new scene objects...
    terrain = Terrain.Terrain(renderers, 100)
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

#    axes = Axes.Axes(renderer)
        
    # Render an image (lights and cameras are created automatically)
    renderWindow.Render()
    
    #FORCE the cameras to a shared, reasonable position
    for renderer in renderers:
        camera = renderer.GetActiveCamera()
        camera.SetPosition([20, 20, 20])
        camera.SetFocalPoint([0, 0, 0]) 

    # Sign up to receive TimerEvent for the timed rendering loop
    renderObserverId = renderWindowInteractor.AddObserver('TimerEvent', __3DRenderingLoop)
    __3DViewLoopTimerId = renderWindowInteractor.CreateRepeatingTimer(30);

    # Set up the custom style for your camera interactor
    # Uncomment one of the following below to select it
    #interactorStyle = InteractorMapUser.InteractorMapUser(renderer, renderWindowInteractor)
    #interactorStyle = Interactor1stPersonUser.Interactor1stPersonUser(renderer, renderWindowInteractor)
    #interactorStyle = Interactor3rdPerson.Interactor3rdPerson(renderer, renderWindowInteractor, bots[1], [0, 7, -10])
    interactorStyle = Interactor1stPersonVuzix.Interactor1stPersonVuzix(renderers, renderWindowInteractor)
    # Now set it as the interactor style for the interactor
    renderWindowInteractor.SetInteractorStyle(interactorStyle)
    interactorStyle.EnabledOn()
    
   
    # Begin mouse interaction
    renderWindowInteractor.Start()
    renderWindowInteractor.Initialize()
    
    # Once done, remove the timer to clean up just to be neat
    renderWindowInteractor.DestroyTimer(__3DViewLoopTimerId) 
    renderWindowInteractor.RemoveObserver(renderObserverId)
    
    pass
