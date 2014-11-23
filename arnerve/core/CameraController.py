'''
Created on Nov 20, 2014

@author: alucard
'''

import vtk

class CameraController():
    
    def __init__(self, renderManager):
        self.renderManager = renderManager
        self.position = [0, 0, 0]
        self.targetPosition = [0, 0, 0]
    
    def __str__(self):
        s = ""
        return s
    
    def SetPosition(self, newPosition):
        for item in self.renderManager.renderers:
            camera = item.GetActiveCamera()
            camera.SetPosition(newPosition[0], newPosition[1], newPosition[2])
    
    def SetTargetPosition(self, newTargetPosition):
        for item in self.renderManager.renderers:
            camera = item.GetActiveCamera()
            camera.SetFocalPoint(newTargetPosition[0], newTargetPosition[1], newTargetPosition[2])