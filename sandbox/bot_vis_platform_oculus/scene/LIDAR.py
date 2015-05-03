'''
Created on Aug 5, 2014

@author: gearsad
'''
import vtk
import numpy
from math import sin,cos
from SceneObject import SceneObject

class LIDAR(SceneObject):
    '''
    A template for drawing a LIDAR point cloud.
    Ref: http://stackoverflow.com/questions/7591204/how-to-display-point-cloud-in-vtk-in-different-colors
    '''
    
    # The point cloud data
    vtkPointCloudPolyData = None
    
    vtkPointCloudPoints = None
    vtkPointCloudDepth = None
    vtkPointCloudCells = None
    
    #The dimensions of the window
    numThetaReadings = None
    numPhiReadings = None
    thetaRange = [0, 0]
    phiRange = [0, 0]
    
    def __init__(self, renderer, minTheta, maxTheta, numThetaReadings, minPhi, maxPhi, numPhiReadings, minDepth, maxDepth, initialValue):
        '''
        Initialize the LIDAR point cloud.
        '''
        # Call the parent constructor
        super(LIDAR,self).__init__(renderer)
        # Cache these
        self.numPhiReadings = numPhiReadings
        self.numThetaReadings = numThetaReadings
        self.thetaRange = [minTheta, maxTheta]
        self.phiRange = [minPhi, maxPhi]
                
        # Create a point cloud with the data 
        self.vtkPointCloudPoints = vtk.vtkPoints()
        self.vtkPointCloudDepth = vtk.vtkDoubleArray()
        self.vtkPointCloudDepth.SetName("DepthArray")
        self.vtkPointCloudCells = vtk.vtkCellArray()
        self.vtkPointCloudPolyData = vtk.vtkPolyData()
        # Set up the structure
        self.vtkPointCloudPolyData.SetPoints(self.vtkPointCloudPoints)
        self.vtkPointCloudPolyData.SetVerts(self.vtkPointCloudCells)
        self.vtkPointCloudPolyData.GetPointData().SetScalars(self.vtkPointCloudDepth)
        self.vtkPointCloudPolyData.GetPointData().SetActiveScalars("DepthArray")
        
        # Build the initial structure
        for x in xrange(0, self.numThetaReadings):
            for y in xrange(0, self.numPhiReadings):
                # Add the point
                point = [1, 1, 1]
                pointId = self.vtkPointCloudPoints.InsertNextPoint(point)
                self.vtkPointCloudDepth.InsertNextValue(1)
                self.vtkPointCloudCells.InsertNextCell(1)
                self.vtkPointCloudCells.InsertCellPoint(pointId)
        # Use the update method to initialize the points with a NumPy matrix
        initVals = numpy.ones((numThetaReadings, numPhiReadings)) * initialValue
        self.UpdatePoints(initVals)

        # Now build the mapper and actor.
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(self.vtkPointCloudPolyData)
        mapper.SetColorModeToDefault()
        mapper.SetScalarRange(minDepth, maxDepth)
        mapper.SetScalarVisibility(1)         
        self.vtkActor.SetMapper(mapper)
        
    def UpdatePoints(self, points2DNPMatrix):
        '''Update the points with a 2D array that is numThetaReadings x numPhiReadings containing the depth from the source'''
        for x in xrange(0, self.numThetaReadings):
            theta = (self.thetaRange[0] + float(x) * (self.thetaRange[1] - self.thetaRange[0]) / float(self.numThetaReadings)) / 180.0 * 3.14159
            for y in xrange(0, self.numPhiReadings):
                phi = (self.phiRange[0] + float(y) * (self.phiRange[1] - self.phiRange[0]) / float(self.numPhiReadings))  / 180.0 * 3.14159
                
                r = points2DNPMatrix[x, y]
                # Polar coordinates to Euclidean space
                point = [r * sin(theta) * cos(phi), r * sin(phi), r * cos(theta) * cos(phi)]
                pointId = y + x * self.numPhiReadings
                self.vtkPointCloudPoints.SetPoint(pointId, point)
        self.vtkPointCloudCells.Modified()
        self.vtkPointCloudPoints.Modified()
        self.vtkPointCloudDepth.Modified()        