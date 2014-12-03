'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject


class Hand(SceneObject):
    '''
    A hand model for the user.
    '''
    
    def __init__(self, renderers, isRightHand):
        '''
        Initialize the user model.
        '''
        # Call the parent constructor
        super(Hand,self).__init__(renderers)
        
        filename = "../scene/media/rhand.stl"
         
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        
        # Do the internal transforms to make it look along unit-z, do it with a quick transform
        trans = vtk.vtkTransform()
        trans.RotateZ(180)
        if isRightHand == False: #Flip with a horizontal flip using a -1 scale
            trans.Scale([-1, 1, 1])

        transF = vtk.vtkTransformPolyDataFilter()
        transF.SetInputConnection(reader.GetOutputPort())
        transF.SetTransform(trans)
         
        self.__mapper = vtk.vtkPolyDataMapper()
        #if vtk.VTK_MAJOR_VERSION <= 5:
        #    self.__mapper.SetInput(reader.GetOutput())
        #else:
        self.__mapper.SetInputConnection(transF.GetOutputPort())
         
        self.vtkActor.SetMapper(self.__mapper)