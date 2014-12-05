'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
from SceneObject import SceneObject

class CameraScreen(SceneObject):
    '''
    A template for loading complex models.
    '''

    # The camera texture
    cameraVtkTexture = None
    
    def __init__(self, renderer, parent, screenDistance, width, height, isActiveCamera = False):
        '''
        Initialize the CameraScreen model.
        If you are going to stream data to it, set isActiveCamera to true in the constructor parameters and pass jpeg data to the update method.
        '''
        # Call the parent constructor
        super(CameraScreen,self).__init__(renderer, parent)
        
        # Create a plane for the camera 
        # Ref: http://www.vtk.org/doc/nightly/html/classvtkPlaneSource.html
        planeSource = vtk.vtkPlaneSource()
        # Defaults work for this, so just push it out a bit
        #planeSource.Push(screenDistance)
        
        # Transform scale it to the right size
        trans = vtk.vtkTransform()
        trans.Scale(width, height, 1)
        trans.Translate(0, 0, screenDistance)
        trans.RotateY(180) # Effectively flipping the UV (texture) mapping so that the video isn't left/right flipped
        transF = vtk.vtkTransformPolyDataFilter()
        transF.SetInputConnection(planeSource.GetOutputPort())
        transF.SetTransform(trans)
        
        # Create a test picture and assign it to the screen for now...
        # Ref: http://vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/Rendering/Python/TPlane.py
        if not isActiveCamera:
            self.__textReader = vtk.vtkPNGReader()
            self.__textReader.SetFileName("../scene/media/semisortedcameralogo.png")
        else:
            self.__textReader = vtk.vtkJPEGReader()
        self.cameraVtkTexture = vtk.vtkTexture()
        self.cameraVtkTexture.SetInputConnection(self.__textReader.GetOutputPort())
        self.cameraVtkTexture.InterpolateOn()        
        
        # Finally assign the mapper and the actor
        planeMapper = vtk.vtkPolyDataMapper()
        planeMapper.SetInputConnection(transF.GetOutputPort())
         
        self.vtkActor.SetMapper(planeMapper)
        self.vtkActor.SetTexture(self.cameraVtkTexture)

    def SetScreenJPEGImage(self, botName, jpegData):
        '''
        TEMPORARY - Write the image to a file and then reroute the textureReader to this file. Need a memorybuffer later. [GearsAD]
        '''
#         fileName = "bot_cam_" + botName + ".jpg"
#         f = open(fileName,"w") #opens file with name of "test.txt"
#         f.write(jpegData)
#         f.close()
        # And update the video frame
        self.__textReader.SetMemoryBufferLength(len(jpegData)) 
        self.__textReader.SetMemoryBuffer(jpegData)
#         self.__textReader.SetFileName(fileName)
        self.__textReader.UpdateInformation()
        self.cameraVtkTexture.SetInputConnection(self.__textReader.GetOutputPort())
        self.vtkActor.SetTexture(self.cameraVtkTexture)