'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class CameraScreen(SceneObject):
    '''
    A template for loading complex models.
    '''

    # The camera texture
    cameraVtkTexture = None
    
    def __init__(self, renderer, parent, screenDistance, width, height):
        '''
        Initialize the CameraScreen model.
        '''
        # Call the parent constructor
        super(CameraScreen,self).__init__(renderer, parent)
        
        # Create a plane for the camera 
        # Ref: http://www.vtk.org/doc/nightly/html/classvtkPlaneSource.html
        planeSource = vtk.vtkPlaneSource()
        # Defaults work for this, so just push it out a bit
        #planeSource.Push(screenDistance)
        
        # Transform scale it to the right size
        trans = vtk.vtkTransform()
        trans.Scale(width, height, 1)
        trans.Translate(0, 0, screenDistance)
        trans.RotateY(180) # Effectively flipping the UV (texture) mapping so that the video isn't left/right flipped
        transF = vtk.vtkTransformPolyDataFilter()
        transF.SetInputConnection(planeSource.GetOutputPort())
        transF.SetTransform(trans)
        
        # Create a test picture and assign it to the screen for now...
        # Ref: http://vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/Rendering/Python/TPlane.py
        textReader = vtk.vtkPNGReader()
        textReader.SetFileName("../scene/media/semisortedcameralogo.png")
        self.cameraVtkTexture = vtk.vtkTexture()
        self.cameraVtkTexture.SetInputConnection(textReader.GetOutputPort())
        self.cameraVtkTexture.InterpolateOn()        
        
        # Finally assign the mapper and the actor
        planeMapper = vtk.vtkPolyDataMapper()
        planeMapper.SetInputConnection(transF.GetOutputPort())
         
        self.vtkActor.SetMapper(planeMapper)
        self.vtkActor.SetTexture(self.cameraVtkTexture)
