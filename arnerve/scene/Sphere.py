'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class Sphere(SceneObject):
    '''
    A template for drawing a sphere. 
    '''

    def __init__(self, renderers, scale = 1, color = [1.0, 0, 0]):
        '''
        Initialize the sphere.
        '''
        # Call the parent constructor
        super(Sphere,self).__init__(renderers)
        
        sphereSource = vtk.vtkSphereSource()
        sphereSource.SetCenter(0.0, 0.0, 0.0)
        sphereSource.SetRadius(scale)
        # Make it a little more defined
        sphereSource.SetThetaResolution(12)
        sphereSource.SetPhiResolution(12)
         
        sphereMapper = vtk.vtkPolyDataMapper()
        sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
         
        self.vtkActor.SetMapper(sphereMapper)
        # Change it to a red sphere
        self.vtkActor.GetProperty().SetColor(color[0], color[1], color[2])
        
    def SetColor(self, color = [1.0, 0, 0]):
        self.vtkActor.GetProperty().SetColor(color[0], color[1], color[2])
        
        
        
        
        
        
    
    