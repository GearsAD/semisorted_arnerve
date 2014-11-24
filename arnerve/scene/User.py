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

class User(SceneObject):
    '''
    A user (for the moment).
    '''

    def __init__(self, renderers, name):
        '''
        Initialize the user model.
        '''
        
        self.name = name
        
        # Call the parent constructor
        super(User,self).__init__(renderers)
        
        self.SetPositionVec3([0, 0, 0])
        
        self.__setupChildren(renderers)
        
    def __setupChildren(self, renderers):
        '''
        Configure the children for this user - camera and other sensors.
        '''
         
        # Create the LIDAR template and set it to the child's offset as well         
        self.kinectSpheres = []
        for i in range(0, 25):
            sphere = Sphere.Sphere(renderers, 0.125, [0.2, 0.2, 1.0])
            sphere.relativePosition = [0, 0, 0]
            # Add it to the bot's children
            self.childrenObjects.append(sphere)
            self.kinectSpheres.append(sphere)
        
        self.headSphere = Sphere.Sphere(renderers, 0.2, [1.0, 0.2, 0.2])
        self.childrenObjects.append(self.headSphere)

        self.lhandSphere = Sphere.Sphere(renderers, 0.15, [0.2, 1.0, 0.2])
        self.childrenObjects.append(self.lhandSphere)
        self.rhandSphere = Sphere.Sphere(renderers, 0.15, [0.2, 1.0, 0.2])
        self.childrenObjects.append(self.rhandSphere)

        self.headPointerCylinder = Cylinder.Cylinder(renderers, 0.05, 0.3, [90, 0, 0], [0, 0, 0.25])
        self.childrenObjects.append(self.headPointerCylinder)

        self.Menu = MenuItemController.MenuItemController(renderers, renderers[0].GetRenderWindow().GetInteractor(), "UserMenu")
        self.Menu.relativePosition = [0, 0, 1]
        self.Menu.BuildTestMenu()
        self.childrenObjects.append(self.Menu)
      
    def UpdateUser(self, update_user):
        '''
        Update the user from a direct LCM frame of this user
        '''
        
        torsoCenter = update_user.kinect.torsoposition.position
        
        #Set the kinect spheres for this user.
        index = 0
        #if(update_user.kinect.istrackingbody):
        for joint in update_user.kinect.rawkinectdata.bodyjoints:
            self.kinectSpheres[index].relativePosition = [joint.position[0], joint.position[1], joint.position[2]]
            if joint.istracking == 1:
                self.kinectSpheres[index].SetColor([0.2, 0.2, 1.0]) #Blue
            else:
                self.kinectSpheres[index].SetColor([0.4, 0.4, 0.4]) #Grey
            index = index + 1
        
        #Set the head.
        self.headSphere.relativePosition = update_user.kinect.headposition.position
        self.headPointerCylinder.relativePosition = update_user.kinect.headposition.position
        
        #Set the hands.
        self.lhandSphere.relativePosition = update_user.kinect.lhandposition.position
        self.rhandSphere.relativePosition = update_user.kinect.rhandposition.position
            
        #Set the oculus to look 'forward'
        headOrient = [0 ,0 ,0]
        headOrient[0] = update_user.oculus.headorientation[0] * 180.0 / 3.14159
        headOrient[1] = update_user.oculus.headorientation[1] * 180.0 / 3.14159
        headOrient[2] = 0
        self.headPointerCylinder.vtkActor.SetOrientation(headOrient[0], headOrient[1], headOrient[2])
            
        self.SetPositionVec3(torsoCenter)
            
            
            
            
            
            
            
            
            
            