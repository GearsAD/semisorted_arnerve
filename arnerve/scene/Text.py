'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class Text(SceneObject):
    '''
    A text object.
    '''

    # The camera texture
    cameraVtkTexture = None
    
    def __init__(self, renderer, parent, text, scale, position):
        '''
        Initialize the CameraScreen model.
        '''
        # Call the parent constructor
        super(Text,self).__init__(renderer, parent)
        
        atext = vtk.vtkVectorText()
        atext.SetText(text)
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(atext.GetOutputPort())
#        self.vtkActor = vtk.vtkFollower()
        self.vtkActor.SetMapper(textMapper)
        self.vtkActor.SetScale(scale, scale, scale)
        self.vtkActor.SetPosition(position)