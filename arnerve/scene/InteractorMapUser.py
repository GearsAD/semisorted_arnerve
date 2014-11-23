'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from InteractorSuperclass import InteractorSuperclass 

class InteractorMapUser(InteractorSuperclass):
    '''
    Inherit the VTK class vtkInteractorStyleUser and extend it to be a 1st-person camera for the observer.
    Ref: http://www.vtk.org/doc/nightly/html/classvtkInteractorStyleUser.html#details
    
    Important details about implementation: http://vtk.1045678.n5.nabble.com/vtkInteractorStyleUser-td2839763.html

    Interactors: http://www.atamai.com/cgi-bin/viewvc.cgi/atamai/classes/PaneFrame.py?diff_format=u&pathrev=OCCIviewer-1-0-99&logsort=cvs&sortby=rev&view=diff&r1=1.25&r2=1.26
    '''
    
    def __init__(self, renderer, iren):
        # Call the parent constructor
        InteractorSuperclass.__init__(self, renderer, iren)

        # Set the camera to look along Z when it is initialized
        camera = self.GetCurrentRenderer().GetActiveCamera()
        camera.SetFocalPoint((0, 0, 0))
        camera.SetPosition((0, 30, -0.01))
        camera.SetViewAngle(60) #Make it a little wider.
                
    def SetCameraPosition(self, posVec3):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        #Calculate the difference between the focal point and the camera
        focal = camera.GetFocalPoint()
        camPos = camera.GetPosition()
        focal = (focal[0] + posVec3[0] - camPos[0], focal[1] + posVec3[1] - camPos[1], focal[2] + posVec3[2] - camPos[2])
        camera.SetPosition(posVec3)
        camera.SetFocalPoint(focal) 
    
    def MouseMoveCallback(self, obj, event):
        # Leave the mouse for picking
        return

    def KeydownCallback(self, obj, event):
        '''
        Responding to keyboard events for now, want something more interactive later.
        Ref: http://portal.nersc.gov/svn/visit/tags/2.6.0/vendor_branches/vtk/src/Examples/GUI/Python/CustomInteraction.py
        '''
        # Get the interactor
        iren = self.GetInteractor()
        if iren is None: return
        
        key = iren.GetKeyCode()
        if key == "8": # Move forward
            self.__MoveForward()
        if key == "5": # Move backward
            self.__MoveBackward()
        if key == "6": # Move right
            self.__MoveRight()
        if key == "4":
            self.__MoveLeft()
        if key == "7":
            self.__MoveIn()
        if key == "9":
            self.__MoveOut()

    def KeyupCallback(self, obj, event):
        return
    
    def __MoveForward(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [0, 0, 1]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
    
    def __MoveBackward(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [0, 0, -1]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
    
    def __MoveRight(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [-1, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()

    def __MoveLeft(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [1, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()

    def __MoveIn(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [0, -1, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()

    def __MoveOut(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [0, 1, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Add(cam, vec, newCam)
        vtk.vtkMath.Add(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
    