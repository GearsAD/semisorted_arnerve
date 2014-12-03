'''
Created on Nov 20, 2014

@author: alucard
'''

import vtk

class CameraController():
    
    def __init__(self, renderManager, eyeWidth = 0.0, FOV = 60, useHalfFOV = False):
        self.renderManager = renderManager
        self.position = [0, 0, 0]
        self.targetPosition = [0, 0, 0]
        self.eyeWidth = eyeWidth
        
        # Do this somewhere.
        for renderer in self.renderManager.renderers:
            camera = renderer.GetActiveCamera()
            camera.SetViewAngle(FOV)
            #camera.UseHorizontalViewAngleOn()
            #camera.SetUseHorizontalViewAngle(FOV) #Make it a little wider.
    
    def __str__(self):
        s = ""
        return s
    
    def SetPosition(self, newPosition):
        if self.renderManager.stereo:
            
            cameraL = self.renderManager.renderers[0].GetActiveCamera()
            cameraL.SetPosition(newPosition[0] + self.eyeWidth / 2, newPosition[1], newPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[0].ResetCameraClippingRange()
                
            cameraR = self.renderManager.renderers[1].GetActiveCamera()
            cameraR.SetPosition(newPosition[0] - self.eyeWidth / 2, newPosition[1], newPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[1].ResetCameraClippingRange()
                
        else:
            camera = self.renderManager.renderers[0].GetActiveCamera()
            camera.SetPosition(newPosition[0], newPosition[1], newPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[0].ResetCameraClippingRange()
    
    def SetTargetPosition(self, newTargetPosition):
        if self.renderManager.stereo:
            
            cameraL = self.renderManager.renderers[0].GetActiveCamera()
            cameraL.SetFocalPoint(newTargetPosition[0] + self.eyeWidth / 2, newTargetPosition[1], newTargetPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[0].ResetCameraClippingRange()
                
            cameraR = self.renderManager.renderers[1].GetActiveCamera()
            cameraR.SetFocalPoint(newTargetPosition[0] - self.eyeWidth / 2, newTargetPosition[1], newTargetPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[1].ResetCameraClippingRange()
                
        else:
            camera = self.renderManager.renderers[0].GetActiveCamera()
            camera.SetFocalPoint(newTargetPosition[0], newTargetPosition[1], newTargetPosition[2])
            # And reset the clipping range
            self.renderManager.renderers[0].ResetCameraClippingRange()
            
    def SetTargetOrientation(self, orientation):
        '''
        Rotate the target about the axes. COMPLETE and check that the transforms are applied in the right sequence
        '''
        for renderer in self.renderManager.renderers:
            camera = renderer.GetActiveCamera()
            camera.SetViewUp([0, 1, 0])
            
            print "[CameraController.py] Seems that there's an issue with the transmitted orientations - need to confirm and fix [GearsAD]"
            camera.Pitch(orientation[0])
            camera.Yaw(orientation[1])
            camera.Roll(-orientation[2])
            
            # And reset the clipping range
            renderer.ResetCameraClippingRange()
