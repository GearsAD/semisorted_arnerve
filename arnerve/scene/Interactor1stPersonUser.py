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
    
    def __init__(self, renderer, iren, userManager, cameraController):
        # Call the parent constructor
        InteractorSuperclass.__init__(self, renderer, iren)
        
        # Keep track of the managers
        self.__userManager = userManager
        self.__cameraController = cameraController
        
        # Finally call the event handler to do a first-call update in case the model doesn't move
        self.MouseMoveCallback(None, None)
        
    def Update(self):
        # Get the current user.
        user = self.__userManager.currentUser
        userCenter = self.__userManager.currentUserModel.vtkActor.GetPosition()
        headRelativePos = [
                           user.kinect.headposition.position[0],
                           user.kinect.headposition.position[1],
                           user.kinect.headposition.position[2]-3,
                           ]
        headRelativeTarget = [
                           user.kinect.headposition.position[0],
                           user.kinect.headposition.position[1],
                           user.kinect.headposition.position[2],
                           ]
#         headRelativeTarget = [headRelativePos[0], headRelativePos[1], headRelativePos[2]+1] #Along unit-z
        #headRelativeTarget = [headRelativePos[0], headRelativePos[1], headRelativePos[2]+1] #Along unit-z
        # Add in the  user's position to get the absolute head position
        for i in range(0,3):
            headRelativePos[i] += userCenter[i]
            headRelativeTarget[i] += userCenter[i]
        self.__cameraController.SetPosition(headRelativePos)
        self.__cameraController.SetTargetPosition(headRelativeTarget)
        headOrient = [
                      user.oculus.headorientation[0] * 180.0 / 3.141,
                      user.oculus.headorientation[1] * 180.0 / 3.141,
                      user.oculus.headorientation[2] * 180.0 / 3.141]
        self.__cameraController.SetTargetOrientation(headOrient)
        return
    
    def MouseMoveCallback(self, obj, event):
        '''
        Do nothing with the mouse here for the moment.
        '''
        
    def KeydownCallback(self, obj, event):
        '''
        Move the user around with the keyboard.
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
        if key == "m":
            self.__OpenMenu()

    def KeyupCallback(self, obj, event):
        return

    def __OpenMenu(self):
        '''
        Tell the user to open the menu.
        '''
        self.__userManager.currentUserModel.OpenMenu()
    
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
    