'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk

class InteractorSuperclass(vtk.vtkInteractorStyle):
    '''
    Inherit the VTK class vtkInteractorStyleUser and build a superclass for all cameras.
    Ref: http://www.vtk.org/doc/nightly/html/classvtkInteractorStyleUser.html#details
    
    Important details about implementation: http://vtk.1045678.n5.nabble.com/vtkInteractorStyleUser-td2839763.html

    Interactors: http://www.atamai.com/cgi-bin/viewvc.cgi/atamai/classes/PaneFrame.py?diff_format=u&pathrev=OCCIviewer-1-0-99&logsort=cvs&sortby=rev&view=diff&r1=1.25&r2=1.26
    '''
    
    def __init__(self, renderer, iren):
        '''
        Initialize the common observers
        '''
        # Add the mouse observer to handle the movement events.
        self.SetCurrentRenderer(renderer)
        #Ref: http://vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/Modelling/Python/SpherePuzzle.py
        self.__obsIDMouseMoveTag = iren.AddObserver("MouseMoveEvent", self.MouseMoveCallback)
        self.__obsIDKeydownTag = self.AddObserver("KeyPressEvent", self.KeydownCallback)
        self.__obsIDKeyupTag = self.AddObserver("KeyReleaseEvent", self.KeyupCallback)
                
    def SetCameraPosition(self, posVec3):
        raise NotImplementedError("SetCameraPosition hasn't been overwritten in " + self.__name__ + ". This is an abstract method, don't call the base.")

    def Disconnect(self):
        '''
        Clear out all the added observers
        '''
        iren = self.GetInteractor()
        iren.RemoveObserver(self.__obsIDMouseMoveTag)
        self.RemoveObserver(self.__obsIDKeydownTag)
        self.RemoveObserver(self.__obsIDKeyupTag)
        
    def MouseMoveCallback(self, obj, event):
        raise NotImplementedError("MouseMoveCallback hasn't been overwritten in " + self.__name__ + ". This is an abstract method, don't call the base.")
 
    def KeydownCallback(self, obj, event):
        raise NotImplementedError("KeydownCallback hasn't been overwritten in " + self.__name__ + ". This is an abstract method, don't call the base.")
 
    def KeyupCallback(self, obj, event):
        raise NotImplementedError("KeyupCallback hasn't been overwritten in " + self.__name__ + ". This is an abstract method, don't call the base.")
