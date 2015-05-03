'''
Created on Aug 5, 2014

@author: gearsad, alucard
@change: Fixed GetOrientation(), Re-factored Code
@version: v0.5
'''
import vtk

class SceneObject(object):
    '''
    This is a basic superclass for any object that will be included in the 3D scene.
    '''
    def __init__(self, renderer):
        '''
        Constructor with the renderer passed in
        '''
        # Initialize all the variables so that they're unique to self
        # The children SceneObjects for this SceneObject - both rotationally and positionally bound to the parent 
        self.childrenObjects = []
        # The positional offset of this object if it is a child 
        self.childPositionOffset = [0, 0, 0]
        # The rotational offset of this object if it is a child
        self.childRotationalOffset = [0, 0, 0]
        # The actor
        # Ref - http://www.vtk.org/doc/nightly/html/classvtkActor.html
        self.vtkActor = vtk.vtkActor()
        renderer.AddActor(self.vtkActor)
        
    def SetPositionVec3(self, positionVec3):
        self.vtkActor.SetPosition(positionVec3[0], positionVec3[1], positionVec3[2])
        # Update all the children
        for sceneObject in self.childrenObjects:
            newLoc = [0, 0, 0]
            newLoc[0] = positionVec3[0] + sceneObject.childPositionOffset[0]
            newLoc[1] = positionVec3[1] + sceneObject.childPositionOffset[1]
            newLoc[2] = positionVec3[2] + sceneObject.childPositionOffset[2]
            sceneObject.SetPositionVec3(newLoc)
    
    def GetPositionVec3(self):
        return self.vtkActor.GetPosition()
    
    def SetOrientationVec3(self, orientationVec3):
        self.vtkActor.SetOrientation(orientationVec3[0], orientationVec3[1], orientationVec3[2])
        # Update all the children
        for sceneObject in self.childrenObjects:
            newOr = [0, 0, 0]
            newOr[0] = orientationVec3[0] + sceneObject.childRotationalOffset[0]
            newOr[1] = orientationVec3[1] + sceneObject.childRotationalOffset[1]
            newOr[2] = orientationVec3[2] + sceneObject.childRotationalOffset[2]
            sceneObject.SetOrientationVec3(newOr)
    
    def GetOrientationVec3(self):
        return self.vtkActor.GetOrientation()