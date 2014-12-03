'''
Created on Nov 11, 2014

@author: alucard
'''

import vtk

from SceneObject import SceneObject
from Text import Text

class MenuItem(SceneObject):
    
    def __init__(self, renderManager, width, height, parent, name, vtkTextureSelected, vtkTextureUnselected, callbackFunction = None, callbackObject = None):
        '''
        Initialize the MenuItem.
        '''
        # Initialize all the variables so that they're unique
        
        self.__renderManager = renderManager
        
        # Call the parent constructor
        super(MenuItem, self).__init__(self.__renderManager.renderers)
        
        # Set selected and unselected textures
        self.__selectedTexture = vtkTextureSelected
        self.__unselectedTexture = vtkTextureUnselected
        
        self.menuItemPadding = [0.0, 0.0, 0.0, 0.0]
        self.parent = parent
        self.name = name
        
        # Default a menu item to be hidden and collapsed.
        self.__isOpen = False
        self.__isVisible = False
            
        self.__planeSource = vtk.vtkPlaneSource()
        self.__transform = vtk.vtkTransform()
        self.__transform.Scale(width, height, 1)
        self.__transformFilter = vtk.vtkTransformPolyDataFilter()
        self.__transformFilter.SetInputConnection(self.__planeSource.GetOutputPort())
        self.__transformFilter.SetTransform(self.__transform)
        
        self.__planeMapper = vtk.vtkPolyDataMapper()
        self.__planeMapper.SetInputConnection(self.__transformFilter.GetOutputPort())
         
        self.vtkActor.SetMapper(self.__planeMapper)
        self.vtkActor.SetTexture(self.__unselectedTexture)
        self.vtkActor.VisibilityOff()
        self.vtkActor.DragableOff()
                
        self.parent.AddMenuItem(self)
            
        self.SetCallback(callbackFunction, callbackObject)
                
        bounds = self.vtkActor.GetBounds()

        self.__menuItemWidth = bounds[1] - bounds[0]
        self.__menuItemHeight = bounds[3] - bounds[2]
        
        # Add the text such that it is centred and at the right x position for the icon on the right of the SAOish texture 
        # (root nodes do not have text, so this is a special case for leaf nodes with a known texture)
        # Below is a HACK
        planeWidth = self.GetWidth()
        textureWidth = 258.0
        textPos = 83.0 
        textOffset = -planeWidth / 2.0 + textPos / textureWidth * planeWidth #Special calc = left edge [which is -width / 2] + pixel position of text [83] / (total pixel width of texture [258]) * total surface width [width]
        
        self.__textItem = Text(self.__renderManager.renderers, self, name, height/4.0, [textOffset, -height * 1.0 / 8.0, 0.01])
        # Turn off picking for the text.
        self.__textItem.vtkActor.PickableOff()
        # Add it to the children
        self.childrenObjects.append(self.__textItem)
        
    def __str__(self):
        '''
        Print the MenuItem
        '''
        s = "Name : " + self.GetName() + "\n"
        s += "Open : " + str(self.GetOpen()) + "\n"
        s += "Visible : " + str(self.GetVisible()) + "\n"
        s += "Width : " + str(self.GetWidth()) + "\n"
        s += "Height : " + str(self.GetHeight()) + "\n"
        s += "Padding : " + str(self.GetPadding()) + "\n"
        s += "Child Menu Item Count : " + str(self.GetChildCount()) + "\n"
        s += "Call Back Function : " + str(self.__calbackFunction) + "\n"
        s += "Call Back Object : " + str(self.__callbackObject) + "\n"
        return s
        
    def GetOpen(self):
        return self.__isOpen
    
    def GetVisible(self):
        return self.__isVisible
    
    def GetWidth(self):
        # Width is returned after adding MenuItem Padding (left and right)
        width = self.menuItemPadding[0] + self.__menuItemWidth + self.menuItemPadding[2]
        return width
    
    def GetHeight(self):
        # Height is returned after adding MenuItem Padding (top and bottom)
        height = self.menuItemPadding[1] + self.__menuItemHeight + self.menuItemPadding[3]
        return height
    
    def GetPadding(self):
        return self.menuItemPadding
    
    def GetParent(self):
        return self.parent
    
    def GetChildCount(self):
        return len(self.childrenObjects)
    
    def GetChildren(self):
        '''
        Create a list of all MenuItem Children
        '''
        children = []
        
        # Get all MenuItem children
        for child in self.childrenObjects:
            if type(child) is MenuItem:
                children.append(child)
        
        return children
    
    def GetName(self):
        return self.name
    
    def SetOpen(self, status):
        self.__isOpen = status
        
    def SetVisible(self, status):
        '''
        Set the MenuItem visibility, set textItem visibility
        '''
        self.__isVisible = status
        
        # Set the MenuItems Visibility and the accompanying text visibility
        if self.__isVisible == True:
            self.vtkActor.VisibilityOn()
            self.__textItem.vtkActor.VisibilityOn()
        if self.__isVisible == False:
            self.vtkActor.VisibilityOff()
            self.__textItem.vtkActor.VisibilityOff()
        
    def SetPadding(self, padding):
        self.__menuItemPadding = padding
    
    def SetPosition(self, position):
        self.SetSceneObjectPosition(position)
        
    def SetName(self, name):
        self.__name = name
    
    def SetCallback(self, callbackFunction, callbackObject):
        '''
        Set the callback for this MenuItem
        '''
        self.__callbackObject = callbackObject
        self.__calbackFunction = callbackFunction
    
    def AddMenuItem(self, menuItem):     
        self.childrenObjects.append(menuItem)
    
    def OpenMenuItem(self):
        '''
        Open the MenuItem, set the visibility and set the texture, set visibility for each child MenuItem
        '''
        self.SetOpen(True)
        self.SetVisible(True)
        self.vtkActor.SetTexture(self.__selectedTexture)
        if self.GetChildCount() > 0:
            for item in self.childrenObjects:
                # Make sure we are only setting MenuItem
                if type(item) is MenuItem:
                    item.SetVisible(True)
    
    def CloseMenuItem(self):
        '''
        Close the MenuItem, set the visibility and set the texture, recursive function
        '''
        self.SetOpen(False)
        self.SetVisible(False)
        self.vtkActor.SetTexture(self.__unselectedTexture)
        if self.GetChildCount() > 0:
            for item in self.childrenObjects:
                # Make sure we are only setting MenuItem
                if type(item) is MenuItem:
                    item.CloseMenuItem()
            
    def CheckActor(self, actor):
        '''
        Check if this MenuItem is picked, return true if it is picked, also fire the MenuItem's callback if it exists.
        '''
        if self.vtkActor is actor: #If the actor is the picked one
            # Click the button.
            if self.__calbackFunction is not None:
                self.__calbackFunction(self.__callbackObject)
            return True
        return False
    
    def GlobalMenuClose(self):
        '''
        Close and remove all references to the menu items.
        '''
        if self.GetChildCount() > 0:
            for item in self.childrenObjects:
                if type(item) is MenuItem:
                    item.GlobalMenuClose()
        self.RemoveSceneObject()