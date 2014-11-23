'''
Created on Nov 20, 2014

@author: alucard
'''

import vtk

class CameraController():
    
    def __init__(self, renderers, newPosition, newTargetPosition):
        self.position = newPosition
        self.targetPosition = newTargetPosition
    
    def __str__(self):
        s = ""
        return s
    
    def SetPosition(self, camera, newPosition):
        camera.SetPosition(newPosition[0], newPosition[1], newPosition[2])
    
    def SetTargetPosition(self, camera, newTargetPosition):
        camera.SetFocalPoint(newTargetPosition[0], newTargetPosition[1], newTargetPosition[2])
        
    def Update(self, renderers, newPosition, newTargetPosition):
        for item in renderers:
            camera = item.GetActiveCamera()
            self.SetPosition(camera, newPosition)
            self.SetTargetPosition(camera, newTargetPosition)