'''
Created on Nov 20, 2014

@author: gearsad
'''

import sys

import vtk

class RenderManager(object):
    '''
    classdocs
    '''

    def __init__(self, name, device, width, height, stereo):
        '''
        Constructor
        '''
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
            #camera = self.rendererCenter.GetActiveCamera()
            #camera.Stereo(1)
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
            self.__InitOculus()
        elif self.device == "Wrap920":
            self.__InitWrap920()
        else: 
            raise Exception("You have not selected a valid display type - Display, Oculus, or Wrap920.")
        
        try:
            self.__InitializeRenderWindowInteractor()
        except:
            print "Unexpected error:", sys.exc_info()[0]
        
        # Sign up to receive TimerEvent for the timed rendering loop
        self.renderObserverId = self.renderWindowInteractor.AddObserver('TimerEvent', self.__3DRenderingLoop)
        
        self.__3DViewLoopTimerId = self.renderWindowInteractor.CreateRepeatingTimer(30)
        
    def Shutdown(self):
        # Once done, remove the timer to clean up just to be neat
        self.interactor.DestroyTimer(self.__3DViewLoopTimerId)
        self.interactor.RemoveObserver(self.renderObserverId)
        
    def __InitDisplay(self, width, height):
        
            # A renderer and render window
            #self.renderer = vtk.vtkRenderer()
            #self.renderWindow = vtk.vtkRenderWindow()
            #self.renderWindow.AddRenderer(self.renderer)
            
            # Make it a little bigger than default
            self.renderWindow.SetSize(width, height)
        
            # An interactor
            #self.renderWindowInteractor = vtk.vtkRenderWindowInteractor()
            #self.renderWindowInteractor.SetRenderWindow(self.renderWindow)
        
        # Create a mapper
        #self.mapper = vtk.vtkPolyDataMapper()

        # Create actor
        #self.actor = vtk.vtkActor()
        #self.actor.SetMapper(self.mapper)

    
    def __InitOculus(self):
        i = 0
        
    def __InitWrap920(self):
        i = 0
        
    def __3DRenderingLoop(self, obj, event):
        '''
        Main loop for rendering at a constant ~30Hz
        '''
        iren = obj
        iren.GetRenderWindow().Render()
    