'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject
from scene import CameraScreen
from scene import LIDAR

from bot_update_t import bot_update_t

class RoverBot(SceneObject):
    '''
    A roverbot.
    '''
    
    def __init__(self, renderers, name):
        '''
        Initialize the bot model.
        '''
        # Call the parent constructor
        super(RoverBot,self).__init__(renderers)
        
        filename = "../scene/media/rover.stl"
        
        self.__name = name
         
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        
        # Do the internal transforms to make it look along unit-z, do it with a quick transform
        trans = vtk.vtkTransform()
        trans.Scale(0.05, 0.05, 0.05)
        trans.RotateX(-90)
        transF = vtk.vtkTransformPolyDataFilter()
        transF.SetInputConnection(reader.GetOutputPort())
        transF.SetTransform(trans)
         
        self.__mapper = vtk.vtkPolyDataMapper()
        #if vtk.VTK_MAJOR_VERSION <= 5:
        #    self.__mapper.SetInput(reader.GetOutput())
        #else:
        self.__mapper.SetInputConnection(transF.GetOutputPort())
         
        self.vtkActor.SetMapper(self.__mapper)
        
        # Set up all the children for this model
        self.__setupChildren(renderers)
        # Set it to [0,0,0] so that it updates all the children
        self.SetSceneObjectPosition([0, 0, 0])
        
    def __setupChildren(self, renderer):
        '''
        Configure the children for this bot - camera and other sensors.
        '''
        # Create a camera screen and set the child's offset.
        self.camScreen = CameraScreen.CameraScreen(renderer, self, 0.5, 4/3, 1)
        self.camScreen.SetSceneObjectPosition([0, 0.25, 0])
        # Add it to the bot's children
        self.childrenObjects.append(self.camScreen)
         
        # Create the LIDAR template and set it to the child's offset as well         
        self.lidar = LIDAR.LIDAR(renderer, self, -45, 45, 180, -12.5, 12.5, 25, 3, 7, 4)
        self.lidar.SetSceneObjectPosition([0, 0.25, 0])
        # Add it to the bot's children
        self.childrenObjects.append(self.lidar)
                 
