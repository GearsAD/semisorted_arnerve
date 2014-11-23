'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class Axes(SceneObject):
    '''
    A template for drawing axes. 
    Shouldn't really be in a class of it's own, but it's cleaner here and like this we can move it easily.
    Ref: http://vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/GUI/Tcl/ProbeWithSplineWidget.tcl 
    '''

    def __init__(self, renderer):
        '''
        Initialize the axes - not the parent version, we're going to assign a vtkAxesActor to it and add it ourselves.
        '''
        # Skip the parent constructor
        #super(Axes,self).__init__(renderer)
        
        # Ref: http://vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/GUI/Tcl/ProbeWithSplineWidget.tcl
        self.vtkActor = vtk.vtkAxesActor()
        self.vtkActor.SetShaftTypeToCylinder()
        self.vtkActor.SetCylinderRadius(0.05)
        self.vtkActor.SetTotalLength(2.5, 2.5, 2.5)
        # Change the font size to something reasonable
        # Ref: http://vtk.1045678.n5.nabble.com/VtkAxesActor-Problem-td4311250.html
        self.vtkActor.GetXAxisCaptionActor2D().GetTextActor().SetTextScaleMode(vtk.vtkTextActor.TEXT_SCALE_MODE_NONE)
        self.vtkActor.GetXAxisCaptionActor2D().GetTextActor().GetTextProperty().SetFontSize(25);
        self.vtkActor.GetYAxisCaptionActor2D().GetTextActor().SetTextScaleMode(vtk.vtkTextActor.TEXT_SCALE_MODE_NONE)
        self.vtkActor.GetYAxisCaptionActor2D().GetTextActor().GetTextProperty().SetFontSize(25);
        self.vtkActor.GetZAxisCaptionActor2D().GetTextActor().SetTextScaleMode(vtk.vtkTextActor.TEXT_SCALE_MODE_NONE)
        self.vtkActor.GetZAxisCaptionActor2D().GetTextActor().GetTextProperty().SetFontSize(25);         
        
        # Add the actor.
        renderer.AddActor(self.vtkActor)    