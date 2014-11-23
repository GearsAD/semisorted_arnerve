'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
import numpy
from SceneObject import SceneObject
from scene import CameraScreen
from scene import LIDAR

class Bot(SceneObject):
    '''
    A template for loading complex models.
    '''

    # The sensors
    camScreen = None
    lidar = None
    
    def __init__(self, renderer):
        '''
        Initialize the bot model.
        '''
        # Call the parent constructor
        super(Bot,self).__init__(renderer)
        
        filename = "../scene/media/bot.stl"
         
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        
        # Do the internal transforms to make it look along unit-z, do it with a quick transform
        trans = vtk.vtkTransform()
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
        self.__setupChildren(renderer)
        # Set it to [0,0,0] so that it updates all the children
        self.SetPositionVec3([0, 0, 0])
        
    def __setupChildren(self, renderer):
        '''
        Configure the children for this bot - camera and other sensors.
        '''
        # Create a camera screen and set the child's offset.
        self.camScreen = CameraScreen.CameraScreen(renderer, 3, 4, 3)
        self.camScreen.childPositionOffset = [0, 2.5, 0]
        # Add it to the bot's children
        self.childrenObjects.append(self.camScreen)
         
        # Create the LIDAR template and set it to the child's offset as well         
        self.lidar = LIDAR.LIDAR(renderer, -90, 90, 180, -22.5, 22.5, 45, 5, 15, 5)
        self.lidar.childPositionOffset = [0, 2.5, 0]
        # Add it to the bot's children
        self.childrenObjects.append(self.lidar)
         
