'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class Cylinder(SceneObject):
    '''
    A template for drawing a cylinder. 
    '''

    def __init__(self, renderer):
        '''
        Initialize the cylinder.
        '''
        # Call the parent constructor
        super(Cylinder,self).__init__(renderer)
        
        cylinderSource = vtk.vtkCylinderSource()
        cylinderSource.SetCenter(0.0, 0.0, 0.0)
        cylinderSource.SetRadius(2.0)
        cylinderSource.SetHeight(8.0)
        # Make it a little more defined
        cylinderSource.SetResolution(24)
         
        cylinderMapper = vtk.vtkPolyDataMapper()
        cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())
         
        self.vtkActor.SetMapper(cylinderMapper)
        # Change it to a red sphere
        self.vtkActor.GetProperty().SetColor(0.8, 0.8, 0.3)
            