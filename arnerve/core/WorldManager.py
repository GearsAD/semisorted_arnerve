'''
Created on Nov 23, 2014

@author: gearsad
'''

from core import RenderManager
from core import CameraController
from core import SceneManager
from core import UserManager
from core import BotManager
from core import RoleManager
from core import LCMManager

from scene import Interactor1stPersonUser

class WorldManager(object):
    '''
    The complete world controller
    '''

    def __init__(self, name, device, width, height):
        '''
        Create the world.
        '''
        #Initialize the RenderManager
        self.renderManager = RenderManager.RenderManager(device, width, height, 0)
        #self.renderManager = RenderManager.RenderManager(device, width, height, device == "Oculus")
        self.renderManager.Initialize()
        
        self.cameraController = CameraController.CameraController(self.renderManager, 0.055)
        
        # TO BE COMPLETED [GearsAD]
        self.roleManager = RoleManager.RoleManager()
        self.botManager = BotManager.BotManager()
        
        self.userManager = UserManager.UserManager(name)
        
        self.sceneManager = SceneManager.SceneManager()

        self.lcmManager = LCMManager.LCMManager()
        
        # Do all the manager attachment to other managers
        self.lcmManager.Attach(self.userManager, self.roleManager)
        self.roleManager.Attach(self.userManager, self.lcmManager)
        self.sceneManager.Attach(self.userManager, self.renderManager)
        self.userManager.Attach(self.botManager, self.roleManager, self.renderManager)


        # Create a test interactor style for the current user.
        # Generally done by the role manager.
        testInteractor = Interactor1stPersonUser.Interactor1stPersonUser(self.renderManager.renderers[0], self.renderManager.renderWindowInteractor, self.userManager, self.cameraController)
        self.renderManager.SetCurrentInteractorStyle(testInteractor)
                
        
    def Start(self):
        self.CreateUpdateLoop(30)
        #self.CreateCommsLoop(10)
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
        self.lcmManager.Update()
        

    def Shutdown(self):
        # Once done, remove the timer to clean up just to be neat
        self.interactor.DestroyTimer(self.__UpdateLoopTimerId)
        self.interactor.RemoveObserver(self.loopObserverId) 
        self.interactor.DestroyTimer(self.__CommsLoopTimerId)
        self.interactor.RemoveObserver(self.loopLCMObserverId) 
        
        
        
        
        
        
        
        
        
           
