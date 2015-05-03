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

    def __init__(self, renderers, radius = 2.0, height = 8.0, rotationXYZ = [0, 0, 0], offsetXYZ = [0, 0, 0]):
        '''
        Initialize the cylinder.
        '''
        # Call the parent constructor
        super(Cylinder,self).__init__(renderers)
        
        cylinderSource = vtk.vtkCylinderSource()
        cylinderSource.SetCenter(0.0, 0.0, 0.0)
        cylinderSource.SetRadius(radius)
        cylinderSource.SetHeight(height)
        # Make it a little more defined
        cylinderSource.SetResolution(24)
        
        # Transform scale it to the right size
        trans = vtk.vtkTransform()
        trans.Scale(1, 1, 1)
        trans.Translate(offsetXYZ[0], offsetXYZ[1], offsetXYZ[2])
        trans.RotateZ(rotationXYZ[2])  
        trans.RotateX(rotationXYZ[0])
        trans.RotateY(rotationXYZ[1])
        transF = vtk.vtkTransformPolyDataFilter()
        transF.SetInputConnection(cylinderSource.GetOutputPort())
        transF.SetTransform(trans)

         
        cylinderMapper = vtk.vtkPolyDataMapper()
        cylinderMapper.SetInputConnection(transF.GetOutputPort())
         
        self.vtkActor.SetMapper(cylinderMapper)
        # Change it to a red sphere
        self.vtkActor.GetProperty().SetColor(0.8, 0.8, 0.3)
            