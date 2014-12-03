'''
Created on Aug 5, 2014

@author: gearsad, alucard
@change: Fixed GetOrientation(), Re-factored Code, added FK [Gears]
@version: v0.5
'''
import vtk

class SceneObject(object):
    '''
    This is a basic superclass for any object that will be included in the 3D scene.
    '''
    def __init__(self, renderers, parent = None):
        '''
        Constructor with the renderer passed in
        '''
        # Initialize all the variables so that they're unique to self
        # The children SceneObjects for this SceneObject - both rotationally and positionally bound to the parent 
        self.childrenObjects = []
       
        # Set the parent for this SceneObject - makes it positionally and rotationally bound
        self.parent = parent

        # The actor
        # Ref - http://www.vtk.org/doc/nightly/html/classvtkActor.html
        self.vtkActor = vtk.vtkActor()
        
        self.__renderers = renderers
        
        # Add the actor to all the renderers
        for renderer in renderers:
            renderer.AddActor(self.vtkActor)
            
    def RemoveSceneObject(self):
        '''
        Remove the actor and the children from the scene.
        '''
        for child in self.childrenObjects:
            child.RemoveSceneObject()
        self.childrenObjects = []
        # Now clear the parent.
        for renderer in self.__renderers:
            renderer.RemoveActor(self.vtkActor)
        self.parent = None
    
    def UpdateFromParent(self):
        '''
        Update the transform matrices from the parent if it exists - part of the forward kinematics of SceneObject.
        '''
        if self.parent is not None:
            self.parent.vtkActor.ComputeMatrix()
            parentMatrix = self.parent.vtkActor.GetMatrix()
            self.vtkActor.SetUserMatrix(parentMatrix)
        for sceneObject in self.childrenObjects:
            sceneObject.UpdateFromParent()            
            
    def SetSceneObjectPosition(self, positionVec3):
        '''
        Set the position of this SceneObject and update the children if they exist - part of the forward kinematics of SceneObject.
        '''
        self.vtkActor.SetPosition(positionVec3[0], positionVec3[1], positionVec3[2])
        # Update all the children)
        self.UpdateFromParent()

    def GetSceneObjectPosition(self):
        '''
        You got it, get the current relative position from the vtkActor. Will be a tuple because VTK likes it like that (rowr!).
        '''
        return self.vtkActor.GetPosition()
            
    def SetSceneObjectOrientation(self, orientationVec3):
        '''
        Set the orientation of this SceneObject and update the children if they exist - part of the forward kinematics of SceneObject.
        '''
        self.vtkActor.SetOrientation(orientationVec3[0], orientationVec3[1], orientationVec3[2])
        # Update all the children
        self.UpdateFromParent()
        