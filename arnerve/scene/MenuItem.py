'''
Created on Nov 11, 2014

@author: alucard
'''

import vtk

from SceneObject import SceneObject

class MenuItem(SceneObject):
    
    def __init__(self, renderers, screenDistance, width, height, parent, name, image, callbackObject = None, callbackFunction = None):
        
        #renderer.AddObserver("LeftButtonPressEvent", self._OnButtonPress)
        
        super(MenuItem, self).__init__(renderers)
        
        self.isOpen = False
        self.isVisible = False
        
        self.menuItemTexture = "../Testbed/media/semisortedcameralogo.png"
        #self.menuItemTexture = image
        
        self.menuItemCenter = [0.0, 0.0, 0.0]
        self.menuItemPadding = [0.0, 0.0, 0.0, 0.0]
        self.menuItemPosition = [0, 0, 0]
        self.childMenuItems = []
        self.parent = parent
        self.name = name
            
        self.planeSource = vtk.vtkPlaneSource()
        
        self.transform = vtk.vtkTransform()
        
        self.transform.Scale(width, height, 1)
        
        self.transformFilter = vtk.vtkTransformPolyDataFilter()
        
        self.transformFilter.SetInputConnection(self.planeSource.GetOutputPort())
        self.transformFilter.SetTransform(self.transform)
  
        self.PNGReader = vtk.vtkPNGReader()
        
        self.PNGReader.SetFileName(self.menuItemTexture)
        
        self.VTKTexture = vtk.vtkTexture()
        
        self.VTKTexture.SetInputConnection(self.PNGReader.GetOutputPort())
        self.VTKTexture.InterpolateOn()
        
        self.planeMapper = vtk.vtkPolyDataMapper()
        self.planeMapper.SetInputConnection(self.transformFilter.GetOutputPort())
         
        self.vtkActor.SetMapper(self.planeMapper)
        self.vtkActor.SetTexture(self.VTKTexture)
        self.vtkActor.VisibilityOff()
        self.vtkActor.DragableOff()
        
        # Create the 3D text and the associated mapper and follower (a type of
        # actor).  Position the text so it is displayed over the origin of the
        # axes.
        atext = vtk.vtkVectorText()
        atext.SetText(name)
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(atext.GetOutputPort())
        self.textActor = vtk.vtkFollower()
        self.textActor.SetMapper(textMapper)
        self.textActor.SetScale(0.2, 0.2, 0.2)
        self.textActor.AddPosition(0, -0.1, 0)
        for item in renderers:
            item.AddActor(self.textActor)
        
        if parent is not None:
            parent.AddMenuItem(self)
            
        self.__callbackObject = callbackObject
        self.__calbackFunction = callbackFunction
        
        bounds = self.vtkActor.GetBounds()

        self.menuItemWidth = bounds[1] - bounds[0]
        self.menuItemHeight = bounds[3] - bounds[2]
        self.menuItemDepth = bounds[5] - bounds[4]
        
        #center = self.vtkActor.GetCenter()
        
        self.menuItemCenter[0] = self.menuItemWidth / 2
        self.menuItemCenter[1] = self.menuItemHeight / 2
        self.menuItemCenter[2] = self.menuItemDepth / 2
        
        position = self.vtkActor.GetPosition()
        
        self.menuItemPosition[0] = position[0]
        self.menuItemPosition[1] = position[1]
        self.menuItemPosition[2] = position[2]
        
    def __str__(self):
        s = "Name : " + self.GetName() + "\n"
        s += "Open : " + str(self.GetOpen()) + "\n"
        s += "Visible : " + str(self.GetVisible()) + "\n"
        s += "Width : " + str(self.GetWidth()) + "\n"
        s += "Height : " + str(self.GetHeight()) + "\n"
        s += "Depth : " + str(self.GetDepth()) + "\n"
        s += "Center : " + str(self.GetCenter()) + "\n"
        s += "Position : " + str(self.GetPosition()) + "\n"
        s += "Padding : " + str(self.GetPadding()) + "\n"
        s += "Texture : " + self.GetTexture() + "\n"
        s += "Child Menu Item Count : " + str(self.GetChildCount()) + "\n"
        return s
        
    def GetOpen(self):
        return self.isOpen
    
    def GetVisible(self):
        return self.isVisible
    
    # Width is returned after adding MenuItem Padding (left and right)
    def GetWidth(self):
        width = self.menuItemPadding[0] + self.menuItemWidth + self.menuItemPadding[2]
        return width
    
    # Height is returned after adding MenuItem Padding (top and bottom)
    def GetHeight(self):
        height = self.menuItemPadding[1] + self.menuItemHeight + self.menuItemPadding[3]
        return height
        
    # Depth is returned without MenuItem Padding
    def GetDepth(self):
        return self.menuItemDepth
    
    def GetCenter(self):
        return self.menuItemCenter
    
    def GetPadding(self):
        return self.menuItemPadding
        
    # Returns position of MenuItem
    def GetPosition(self):
        return self.menuItemPosition

    def GetTexture(self):
        return self.menuItemTexture
    
    def GetChildCount(self):
        return len(self.childMenuItems)
    
    def GetName(self):
        return self.name
    
    def SetOpen(self, status):
        self.isOpen = status
        
    def SetVisible(self, status):
        self.isVisible = status
        if self.isVisible == True:
            self.vtkActor.VisibilityOn()
        if self.isVisible == False:
            self.vtkActor.VisibilityOff()
        
    def SetWidth(self, width):
        self.menuItemWidth = width
    
    def SetHeight(self, height):
        self.menuItemHeight = height
        
    def SetDepth(self, depth):
        self.menuItemDepth = depth
        
    def SetPadding(self, padding):
        self.menuItemPadding = padding
    
    def SetPosition(self, position):
        self.menuItemPosition = position
        self.vtkActor.SetPosition(self.menuItemPosition)
        #Move the text
        self.textActor.SetPosition(self.menuItemPosition)
        
    def SetName(self, name):
        self.name = name
    
    def AddMenuItem(self, menuItem):
        self.childMenuItems.append(menuItem)
    
    def OpenMenuItem(self):
        self.SetOpen(True)
        self.SetVisible(True)
        if len(self.childMenuItems) > 0:
            for item in self.childMenuItems:
                item.SetVisible(True)
    
    def CloseMenuItem(self):
        self.SetOpen(False)
        self.SetVisible(False)
        if len(self.childMenuItems) > 0:
            for item in self.childMenuItems:
                item.CloseMenuItem()
            
    def CheckActor(self, actor):
        if self.vtkActor is actor:
            # Click the button.
            if(self.__calbackFunction):
                self.__calbackFunction(self.__callbackObject)
            return True
        return False
            
    def CloseUnselectedMenuItems(self):
        if self.parent is not None:
            for item in self.parent.childMenuItems:
                if item is not self:
                    item.SetOpen(False)
                    item.SetVisible(False)
    
    def SetParentMenuItemPositions(self, newPosition):
        self.SetPosition(newPosition)
        if self.parent is not None:
            position = [newPosition[0], newPosition[1], newPosition[2]]
            position[0] += -(self.GetWidth() / 2) - (self.parent.GetWidth() / 2)
            position[1] = 0.0
            position[2] = self.GetDepth()
            self.parent.SetParentMenuItemPositions(position)
    
    def SetChildMenuItemPositions(self):
        if len(self.childMenuItems) > 0:
            totalHeight = 0.0
            for item in self.childMenuItems:
                totalHeight += item.GetHeight()
            totalHeight = totalHeight / 2
            for item in self.childMenuItems:
                position = [0.0, 0.0, 0.0]
                position[0] = (item.GetWidth() / 2) + (item.parent.GetWidth() / 2)
                position[1] = totalHeight - (item.GetHeight() / 2)
                position[2] = item.parent.GetDepth()
                totalHeight -= item.GetHeight()
                item.SetPosition(position)
    
    def GlobalMenuClose(self):
        if self.GetChildCount() > 0:
            for item in self.childMenuItems:
                item.GlobalMenuClose()
        self.SetOpen(False)
        self.SetVisible(False)