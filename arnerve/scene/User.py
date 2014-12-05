'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject
from scene import Sphere
from scene import Cylinder
from user_update_t import user_update_t
from scene import MenuItem
from scene import MenuItemController
from scene import Hand
from math import sin

class User(SceneObject):
    '''
    A user (for the moment).
    '''

    def __init__(self, botManager, roleManager, renderManager, name):
        '''
        Initialize the user model.
        '''
        
        self.__renderManager = renderManager
        
        self.name = name
        
        # Track the bot and role manager for the menu
        self.__botManager = botManager
        self.__roleManager = roleManager
        
        # Call the parent constructor
        super(User,self).__init__(self.__renderManager.renderers)
                
        self.__setupChildren(self.__renderManager.renderers)
        
        # By default center his torso at 1 metre up.
        self.SetSceneObjectPosition([0, 0, 0])
        
        self.__timeUpdate = 0.0
                
    def __setupChildren(self, renderers):
        '''
        Configure the children for this user - camera and other sensors.
        '''
         
        # Create the LIDAR template and set it to the child's offset as well         
        self.kinectSpheres = []
        for i in range(0, 25):
            sphere = Sphere.Sphere(renderers, 0.05, [0.2, 0.2, 1.0])
            sphere.SetSceneObjectPosition([0, 0, 0])

            # Add it to the bot's children
            self.childrenObjects.append(sphere)
            self.kinectSpheres.append(sphere)
            
        
        # Turn off the spheres for the hands and head.
        hiddenJoints = [3, 7, 11, 21, 22, 23, 24]
        for hiddenIndex in hiddenJoints:
            self.kinectSpheres[hiddenIndex].vtkActor.VisibilityOff()

#         self.headSphere = Sphere.Sphere(renderers, 0.15, [1.0, 0.2, 0.2])
#         self.headSphere.SetSceneObjectPosition([0, 0, 0])
#         self.childrenObjects.append(self.headSphere)

        self.lHand = Hand.Hand(renderers, False)
        self.lHand.SetSceneObjectPosition([0, 0, 0])
        self.childrenObjects.append(self.lHand)
        self.rHand = Hand.Hand(renderers, True)
        self.rHand.SetSceneObjectPosition([0, 0, 0])
        self.childrenObjects.append(self.rHand)
        
        # Create a menu for the user.
        self.__menu = MenuItemController.MenuItemController(self.__botManager, self.__roleManager, self.__renderManager, self, renderers[0].GetRenderWindow().GetInteractor(), "UserMenu")
        self.__menu.SetSceneObjectPosition([0, 0, 0.5])
        self.__menu.SetSceneObjectOrientation([0, 180, 0])

#         self.headPointerCylinder = Cylinder.Cylinder(renderers, 0.05, 0.3, [90, 0, 0], [0, 0, 0.25])
#         self.headPointerCylinder.SetSceneObjectPosition([0, 0, 0])
#         self.childrenObjects.append(self.headPointerCylinder)

#         self.Menu = MenuItemController.MenuItemController(renderers, renderers[0].GetRenderWindow().GetInteractor(), "UserMenu")
#         self.Menu.relativePosition = [0, 0, 1]
#         self.Menu.BuildTestMenu()
#         self.childrenObjects.append(self.Menu)
    
    def Update(self, isLeftHandSelecting):
        '''
        Update the current user - specifically the current user, do not run this for every user.
        '''
        
        #HACK
        self.__timeUpdate += 0.03
        self.lHand.SetSceneObjectPosition([0, 0.5 * sin(2.0 * 3.141 * self.__timeUpdate / 4.0), 0])
        
        if(self.__menu.GetOpen() == True):
            # Use the bounds to get a quick 'centroid' measurement that is absolute
            bounds = self.lHand.vtkActor.GetBounds()
            handPos = [(bounds[0] + bounds[1])/ 2.0, (bounds[2] + bounds[3])/ 2.0, (bounds[4] + bounds[5])/ 2.0]
            
            self.__menu.UpdateMenuSelect(handPos, isLeftHandSelecting)
      
    def UpdaxteUserFromLCM(self, update_user):
        '''
        Update the user from a direct LCM frame of this user
        '''
        # Get the torso center and the forward vector
        torsoCenter = update_user.kinect.torsoposition.position
        forwardVec = list(update_user.kinect.forwardvec)
        
        vtk.vtkMath.Normalize(forwardVec) #It isn't normalized, need to do that for the menu.
        
        #Set the kinect spheres for this user.
        index = 0
        #if(update_user.kinect.istrackingbody):
        for joint in update_user.kinect.rawkinectdata.bodyjoints:
            self.kinectSpheres[index].SetSceneObjectPosition([joint.position[0], joint.position[1], joint.position[2]])
            if joint.istracking == 1:
                self.kinectSpheres[index].SetColor([0.2, 0.2, 1.0]) #Blue
            else:
                self.kinectSpheres[index].SetColor([0.4, 0.4, 0.4]) #Grey
            index = index + 1
        
        #Set the head.
        #self.headSphere.SetSceneObjectPosition(update_user.kinect.headposition.position)
#         self.headPointerCylinder.SetSceneObjectPosition(update_user.kinect.headposition.position)
        
        #Set the hands.
        self.lHand.SetSceneObjectPosition(update_user.kinect.lhandposition.position)
        self.rHand.SetSceneObjectPosition(update_user.kinect.rhandposition.position)

        # Update the menu position 0.5 meter in front of you and 1 metre above you (roughly body chest height)
        vtk.vtkMath.MultiplyScalar(forwardVec, 0.5)
        forwardVec[2] += 1.0
        self.__menu.SetSceneObjectPosition(forwardVec)
        
        # Update all positions
        self.SetSceneObjectPosition(self.GetSceneObjectPosition())

    def SetHandVisibility(self, boolVisible):
        '''
        Set the hand visibility of the user.
        '''
        if boolVisible is True:
            self.lHand.vtkActor.VisibilityOn()
            self.rHand.vtkActor.VisibilityOn()
        else:        
            self.lHand.vtkActor.VisibilityOff()
            self.rHand.vtkActor.VisibilityOff()
        
    def OpenMenu(self):
        '''
        Open the user menu
        '''
        # Show the users hands.
        self.SetHandVisibility(True) 
        if(self.__menu.GetOpen() == False):
            self.__menu.OpenMenu()
           
            