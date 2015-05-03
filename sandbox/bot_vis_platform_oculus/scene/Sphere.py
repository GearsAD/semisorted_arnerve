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

    def __init__(self, renderer):
        '''
        Initialize the sphere.
        '''
        # Call the parent constructor
        super(Sphere,self).__init__(renderer)
        
        sphereSource = vtk.vtkSphereSource()
        sphereSource.SetCenter(0.0, 0.0, 0.0)
        sphereSource.SetRadius(4.0)
        # Make it a little more defined
        sphereSource.SetThetaResolution(24)
        sphereSource.SetPhiResolution(24)
         
        sphereMapper = vtk.vtkPolyDataMapper()
        sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
         
        self.vtkActor.SetMapper(sphereMapper)
        # Change it to a red sphere
        self.vtkActor.GetProperty().SetColor(1.0, 0.0, 0.0)
            