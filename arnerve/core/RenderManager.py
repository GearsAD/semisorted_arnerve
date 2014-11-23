'''
Created on Nov 20, 2014

@author: gearsad
'''

import sys

import vtk

class RenderManager(object):

    def __init__(self, name, device, width, height, stereo):
        self.name = name
        self.device = device
        self.width = width
        self.height = height
        self.stereo = stereo
        self.renderers = [] 
        
    def __CreateRenderer(self):        
        if self.stereo == True:
            self.rendererLeft = vtk.vtkRenderer()
            self.rendererLeft.SetViewport(0.0, 0.0, 0.5, 1.0)
            self.rendererRight = vtk.vtkRenderer()
            self.rendererRight.SetViewport(0.5, 0.0, 1.0, 1.0)
            self.renderers.append(self.rendererLeft)
            self.renderers.append(self.rendererRight)
            return
        if self.stereo == False:
            self.rendererCenter = vtk.vtkRenderer()
            self.renderers.append(self.rendererCenter)
            return
        
    def __CreateRenderWindow(self):
        self.renderWindow = vtk.vtkRenderWindow()
        for item in self.renderers:
            self.renderWindow.AddRenderer(item)
    
    def __CreateRenderWindowInteracter(self):
        self.renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        self.renderWindowInteractor.SetRenderWindow(self.renderWindow)
        
    def __InitializeRenderWindowInteractor(self):
        self.renderWindowInteractor.Initialize()
    
    def __CreateRenderLoop(self, frequency):
        self.renderObserverId = self.renderWindowInteractor.AddObserver('TimerEvent', self.__3DRenderingLoop)
        self.__3DViewLoopTimerId = self.renderWindowInteractor.CreateRepeatingTimer(30)
    
    def __3DRenderingLoop(self, obj, event):
        iren = obj
        iren.GetRenderWindow().Render()
        
    def Initialize(self):
        try:
            self.__CreateRenderer()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
        try:
            self.__CreateRenderWindow()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
        try:
            self.__CreateRenderWindowInteracter()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
        if self.device == "Display":
            self.__InitDisplay(self.width, self.height)
        elif self.device == "Oculus":
            self.__InitOculus(self.width, self.height)
        elif self.device == "Wrap920":
            self.__InitWrap920(self.width, self.height)
        else: 
            raise Exception("You have not selected a valid display type - Display, Oculus, or Wrap920.")
        
        try:
            self.__InitializeRenderWindowInteractor()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            
        try:
            self.__CreateRenderLoop(10)
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
    def Shutdown(self):
        # Once done, remove the timer to clean up just to be neat
        self.interactor.DestroyTimer(self.__3DViewLoopTimerId)
        self.interactor.RemoveObserver(self.renderObserverId)
        
    def __InitDisplay(self, width, height):
        self.renderWindow.SetSize(width, height)
    
    def __InitOculus(self, width, height):
        self.renderWindow.SetSize(width, height)
        
    def __InitWrap920(self, width, height):
        self.renderWindow.SetSize(width, height)
    