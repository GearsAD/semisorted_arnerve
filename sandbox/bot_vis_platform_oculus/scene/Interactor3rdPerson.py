'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from InteractorSuperclass import InteractorSuperclass

class Interactor3rdPerson(InteractorSuperclass):
    '''
    Inherit the VTK class vtkInteractorStyleUser and extend it to be a 3rd-person camera that tracks a specified SceneObject.
    This class will only track the azimuth (heading) because we want to fix the up vector to make viewing easier (as was done in ARX)
    
    Ref: http://www.vtk.org/doc/nightly/html/classvtkInteractorStyleUser.html#details
    
    Important details about implementation: http://vtk.1045678.n5.nabble.com/vtkInteractorStyleUser-td2839763.html

    Interactors: http://www.atamai.com/cgi-bin/viewvc.cgi/atamai/classes/PaneFrame.py?diff_format=u&pathrev=OCCIviewer-1-0-99&logsort=cvs&sortby=rev&view=diff&r1=1.25&r2=1.26
    '''
        
    # The tracked object.
    __trackedObject = None
    
    __camOffsetVec3 = [0, 0, 0]
    
    def __init__(self, renderer, iren, trackedSceneObject, cameraOffsetVec3):
        # Call the parent constructor
        InteractorSuperclass.__init__(self, renderer, iren)
                
        # Set the tracked object and the offset
        self.__trackedObject = trackedSceneObject
        self.__camOffsetVec3 = cameraOffsetVec3

        camera = self.GetCurrentRenderer().GetActiveCamera()
        camera.SetRoll(0)
        camera.SetViewAngle(60) #Make it a little wider.

        # Do a first pass call in case the object doesn't move
        self.MouseMoveCallback(None, None)
        
        #Ref: http://www.vtk.org/doc/nightly/html/classvtkObject.html
        self.__trackingId = self.__trackedObject.vtkActor.AddObserver("ModifiedEvent", self.TrackedObjectMovedCallback)
        
        # In the event that the object doesn't move, update the frame now
        self.TrackedObjectMovedCallback(self.__trackedObject, "ModifiedEvent")
        
    def SetCameraPosition(self, posVec3):
        # Do nothing, this is a bound camera
        return
    
    def Disconnect(self):
        # Call the parent Disconnect() method
        super(Interactor3rdPerson,self).Disconnect()        
        # Remove the tracking
        self.__trackedObject.vtkActor.RemoveObserver(self.__trackingId)
        
    def TrackedObjectMovedCallback(self, obj, event):
        # Get the interactor
        iren = self.GetInteractor()

        # Get the active camera
        camera = self.GetCurrentRenderer().GetActiveCamera()

        # Get the tracked object's orientation and position
        objRot = self.__trackedObject.vtkActor.GetOrientation()
        objPos = self.__trackedObject.vtkActor.GetPosition()
        
        # Reset the focal point to the center of the object and the camera position to the absolute offset
        camera.SetFocalPoint(objPos)
        camera.SetPosition(objPos[0] + self.__camOffsetVec3[0], objPos[1] + self.__camOffsetVec3[1], objPos[2] + self.__camOffsetVec3[2])
        
        # Final azimuthal (heading) rotation
        # Set the camera's up to unit-y so that we rotate around that only,
        # otherwise it will rotate around the orthogonal axes of the focal point->camera vector
        camera.SetViewUp([0, 1, 0])
        # Rotate the camera heading
        camera.Azimuth(objRot[1])
        
        # Update the clipping range of the camera
        self.GetCurrentRenderer().ResetCameraClippingRange()
        
    def MouseMoveCallback(self, obj, event):
        return
    
    def KeyupCallback(self, obj, event):
        return
    
    def KeydownCallback(self, obj, event):
        return    