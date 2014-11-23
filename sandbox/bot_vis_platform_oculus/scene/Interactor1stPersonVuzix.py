'''
Created on Aug 5, 2014

@author: gearsad
'''
import sys
sys.path.append('../')

import vtk
import lcm_channel
from lcm_channel import oculus_headtracker
from InteractorSuperclass import InteractorSuperclass 

class Interactor1stPersonVuzix(InteractorSuperclass):
    '''
    Inherit the VTK class vtkInteractorStyleUser and extend it to be a 1st-person camera for the observer.
    Ref: http://www.vtk.org/doc/nightly/html/classvtkInteractorStyleUser.html#details
    
    Important details about implementation: http://vtk.1045678.n5.nabble.com/vtkInteractorStyleUser-td2839763.html

    Interactors: http://www.atamai.com/cgi-bin/viewvc.cgi/atamai/classes/PaneFrame.py?diff_format=u&pathrev=OCCIviewer-1-0-99&logsort=cvs&sortby=rev&view=diff&r1=1.25&r2=1.26
    '''
    
    def __init__(self, renderers, iren):
        # Call the parent constructor
        InteractorSuperclass.__init__(self, renderers, iren)
        
        self.renderers = renderers
        # Add an LCM channel here
        self.__oculus_chan = lcm_channel.oculus_headtracker.OculusController()
                
        # Add a timer to monitor the updates
        self.__headtrackerObserverId = iren.AddObserver('TimerEvent', self.__HeadTrackingLoop)
        self.__headtrackerTimerId = iren.CreateRepeatingTimer(10);
        
        for renderer in renderers:
            camera = renderer.GetActiveCamera()
            camera.SetViewAngle(70) #Make it a little wider.
        
        # Finally call the event handler to do a first-call update in case the model doesn't move
        self.MouseMoveCallback(None, None)
        
    def __HeadTrackingLoop(self, obj, event):
        '''
        Main loop for reading the LCM channel updates with the head tracking
        '''
        #Update the LCM channel
        self.__oculus_chan.Update()
        #Update the current camera orientation
        # Rotate the focal point around (yaw = x) and (pitch =y) by a factor of the mouse differentials dx and dy
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
            
            # Yaw changes in a negative direction but the pitch is correct
            curPos = camera.GetPosition()
            camera.SetFocalPoint(curPos[0], curPos[1], curPos[2] + 1.0)
            camera.SetViewUp([0, 1, 0])
            camera.Pitch(self.__oculus_chan.HeadTrackingOrientation[2]);
            camera.Yaw(self.__oculus_chan.HeadTrackingOrientation[1]);
    #        camera.SetRoll(self.__lcm_chan.HeadTrackingOrientation[0]);
                    
            # Update the clipping range of the camera
            renderer.ResetCameraClippingRange()
        

    def Disconnect(self):
        # Call the parent Disconnect() method
        super(Interactor1stPersonVuzix,self).Disconnect()        
        # Remove the tracking
        self.__trackedObject.vtkActor.RemoveObserver(self.__headtrackerObserverId)
        # Clean up LCM
        self.__oculus_chan.Disconnect()
        
    def SetCameraPosition(self, posVec3):
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
            #Calculate the difference between the focal point and the camera
            focal = camera.GetFocalPoint()
            camPos = camera.GetPosition()
            focal = (focal[0] + posVec3[0] - camPos[0], focal[1] + posVec3[1] - camPos[1], focal[2] + posVec3[2] - camPos[2])
            camera.SetPosition(posVec3)
            camera.SetFocalPoint(focal) 
    
    def MouseMoveCallback(self, obj, event):
        # Do nothing
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
        if key == "h": # Move forward
            self.__MoveForward()
        if key == "g": # Move forward
            self.__MoveBackward()
        if key == "t": # Move right
            self.__MoveUp()
        if key == "i":
            self.__MoveDown()

    def KeyupCallback(self, obj, event):
        return
    
    def __MoveForward(self):
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
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
            renderer.ResetCameraClippingRange()

    def __MoveBackward(self):
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
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
            renderer.ResetCameraClippingRange()
    
    def __MoveUp(self):
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
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
            renderer.ResetCameraClippingRange()
        
    def __MoveUp(self):
        for renderer in self.renderers:
            camera = renderer.GetActiveCamera()
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
            renderer.ResetCameraClippingRange()
