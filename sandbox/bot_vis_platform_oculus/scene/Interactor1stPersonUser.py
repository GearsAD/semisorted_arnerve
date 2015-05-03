'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from InteractorSuperclass import InteractorSuperclass 

class Interactor1stPersonUser(InteractorSuperclass):
    '''
    Inherit the VTK class vtkInteractorStyleUser and extend it to be a 1st-person camera for the observer.
    Ref: http://www.vtk.org/doc/nightly/html/classvtkInteractorStyleUser.html#details
    
    Important details about implementation: http://vtk.1045678.n5.nabble.com/vtkInteractorStyleUser-td2839763.html

    Interactors: http://www.atamai.com/cgi-bin/viewvc.cgi/atamai/classes/PaneFrame.py?diff_format=u&pathrev=OCCIviewer-1-0-99&logsort=cvs&sortby=rev&view=diff&r1=1.25&r2=1.26
    '''
    
    def __init__(self, renderer, iren):
        # Call the parent constructor
        InteractorSuperclass.__init__(self, renderer, iren)
                
        # Finally call the event handler to do a first-call update in case the model doesn't move
        self.MouseMoveCallback(None, None)
        
    def SetCameraPosition(self, posVec3):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        #Calculate the difference between the focal point and the camera
        focal = camera.GetFocalPoint()
        camPos = camera.GetPosition()
        focal = (focal[0] + posVec3[0] - camPos[0], focal[1] + posVec3[1] - camPos[1], focal[2] + posVec3[2] - camPos[2])
        camera.SetPosition(posVec3)
        camera.SetFocalPoint(focal) 
    
    def MouseMoveCallback(self, obj, event):
        # Get the interactor
        iren = self.GetInteractor()
        if iren is None: return
        
        # Ref: http://portal.nersc.gov/svn/visit/trunk/vendor_branches/vtk/src/Rendering/vtkInteractorStyleTrackballCamera.cxx
        dx = iren.GetEventPosition()[0] - iren.GetLastEventPosition()[0];
        dy = iren.GetEventPosition()[1] - iren.GetLastEventPosition()[1];
        
        # Rotate the focal point around (yaw = x) and (pitch =y) by a factor of the mouse differentials dx and dy
        camera = self.GetCurrentRenderer().GetActiveCamera()
        camera.SetRoll(0)
        
        screenSize = iren.GetRenderWindow().GetSize()
        
        # Yaw changes in a negative direction but the pitch is correct
        camera.Yaw(-float(dx) / float(screenSize[0]) * 360 * 2.0);
        camera.Pitch(float(dy) / float(screenSize[1]) * 180 / 2.0);
                
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()

        # Move it to the center of the screen again so we stay away from the bounds.
        #iren.GetRenderWindow().SetCursorPosition(512, 384)

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

    def KeyupCallback(self, obj, event):
        return
    
    def __MoveForward(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        vec = [0, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Subtract(focal, cam, vec)
        vtk.vtkMath.Normalize(vec)
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
        vec = [0, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Subtract(focal, cam, vec)
        vtk.vtkMath.Normalize(vec)
        vtk.vtkMath.Subtract(cam, vec, newCam)
        vtk.vtkMath.Subtract(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
    
    def __MoveRight(self):
        camera = self.GetCurrentRenderer().GetActiveCamera()
        cam = camera.GetPosition()
        focal = camera.GetFocalPoint()
        up = [0, 1, 0] #We don't want roll
        vec = [0, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Subtract(focal, cam, vec)
        vec[1] = 0 #We don't want roll
        vtk.vtkMath.Normalize(vec)
        vtk.vtkMath.Cross(vec, up, vec)
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
        up = [0, 1, 0] #We don't want roll
        vec = [0, 0, 0]
        newCam = [0, 0, 0]
        newFocal = [0, 0, 0]
        vtk.vtkMath.Subtract(focal, cam, vec)
        vec[1] = 0 #We don't want roll
        vtk.vtkMath.Normalize(vec)
        vtk.vtkMath.Cross(vec, up, vec)
        vtk.vtkMath.Subtract(cam, vec, newCam)
        vtk.vtkMath.Subtract(focal, vec, newFocal)
        camera.SetPosition(newCam)
        camera.SetFocalPoint(newFocal)        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
    