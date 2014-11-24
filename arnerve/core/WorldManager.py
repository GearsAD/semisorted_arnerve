'''
Created on Nov 23, 2014

@author: gearsad
'''

from core import RenderManager
from core import CameraController
from core import SceneManager
from LCMUserHerderController import LCMUserHerderController

class WorldManager(object):
    '''
    The complete world controller
    '''

    def __init__(self, name, device, width, height):
        '''
        Create the world.
        '''
        #Initialize the RenderManager
        self.renderManager = RenderManager.RenderManager(device, width, height, device == "Oculus")
        self.renderManager.Initialize()
        
        self.cameraController = CameraController.CameraController(self.renderManager)
        
        self.sceneManager = SceneManager.SceneManager(self.renderManager, name)
        
        self.lcmController = LCMUserHerderController(self.sceneManager.userManager)
        
    def Start(self):
        self.CreateUpdateLoop(30)
        self.CreateCommsLoop(10)
        self.renderManager.renderWindowInteractor.Start()

    def CreateUpdateLoop(self, frequency):
        self.loopObserverId = self.renderManager.renderWindowInteractor.AddObserver('TimerEvent', self.WorldUpdate)
        self.__UpdateLoopTimerId = self.renderManager.renderWindowInteractor.CreateRepeatingTimer(frequency)

    def CreateCommsLoop(self, frequency):
        self.loopLCMObserverId = self.renderManager.renderWindowInteractor.AddObserver('TimerEvent', self.CommsUpdate)
        self.__CommsLoopTimerId = self.renderManager.renderWindowInteractor.CreateRepeatingTimer(frequency)

    def WorldUpdate(self, obj, event):
        #Update the render
        self.renderManager.RenderUpdate()

    def CommsUpdate(self, obj, event):
        #Update the LCM controller
        self.lcmController.Update()
        

    def Shutdown(self):
        # Once done, remove the timer to clean up just to be neat
        self.interactor.DestroyTimer(self.__UpdateLoopTimerId)
        self.interactor.RemoveObserver(self.loopObserverId) 
        self.interactor.DestroyTimer(self.__CommsLoopTimerId)
        self.interactor.RemoveObserver(self.loopLCMObserverId) 
        
        
        
        
        
        
        
        
        
           
