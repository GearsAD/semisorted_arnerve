'''
Created on Nov 12, 2014

@author: alucard
'''

import vtk

from SceneObject import SceneObject
from scene import MenuItem

class MenuItemController(SceneObject):
    
    def __init__(self, botManager, roleManager, renderManager, parent, iren, menuName):
        '''
        Initialize the MenuItemController.
        '''
        # Initialize all the variables so that they're unique
        self.__renderManager = renderManager
        
        # Call the parent constructor
        super(MenuItemController, self).__init__(self.__renderManager.renderers, parent)
        
        # Reference the botManager
        self.__botManager = botManager
        # Reference the roleManager
        self.__roleManager = roleManager
        
        self.__pickerHandle = iren.AddObserver("EndPickEvent", self._OnPickEvent)
        
        self.name = menuName
        
        self.selectedNode = None
        self.isOpen = False
    
    def __str__(self):
        s = "Open : " + str(self.GetOpen()) + "\n"
        return s
    
    def Disconnect(self):
        iren = self.GetInteractor()
        iren.RemoveObserver(self.__pickerHandle)
    
    def _OnPickEvent(self, obj, event):
        picker = obj.GetPicker()
        actor = picker.GetActor()
        if actor is not None:
            self.CheckPick(actor)
     
    def GetOpen(self):
        return self.isOpen
    
    def GetWidth(self):
        return 0
    
    def SetOpen(self, state):
        self.isOpen = state
        
    def AddMenuItem(self, newMenuItem):
        self.childrenObjects.append(newMenuItem)
    
    def OpenMenu(self):
        '''
        Build the menu as it's opened and set it to be visible.
        '''
        self.__BuildMenu()
        self.SetOpen(True)
        self.__SetInitialOptionsHeight()
        
        # Open the base menu item.
        self.__ActionMenuItem(self.__baseMenuItem)
        
    def __SetInitialOptionsHeight(self):
        '''
        Set the position if more than one root node is used, accounts for an even/uneven number of entries
        '''
        
        # Make sure there are nodes
        if len(self.childrenObjects) > 0:
            totalHeight = 0.0
            
            # Get the total height
            for item in self.childrenObjects:
                totalHeight += item.GetHeight()
            
            # Halve height to position nodes
            totalHeight = totalHeight / 2
            
            # Place all nodes at their calculated positions
            for item in self.childrenObjects:
                position = [0.0, 0.0, 0.0]
                position[0] = 0.0
                position[1] = totalHeight - (item.GetHeight() / 2)
                position[2] = 0.0
                
                totalHeight -= item.GetHeight()
                
                item.SetSceneObjectPosition(position)
            
    def CloseMenu(self):
        '''
        Close the menu and remove all references to nodes.
        '''
        self.SetOpen(False)
        
        for item in self.childrenObjects:
            item.GlobalMenuClose()
            
        # Remove all references to the menu so it is garbage collected.
        self.selectedNode = None
        self.childrenObjects = []
        
#     def CloseCurrentMenuItem(self):
#         if type(self.selectedNode.parent) is MenuItemController:
#             self.selectedNode = None
#             self.SetMenuItemControllerMenuItemLocation()
#             for item in self.childrenObjects:
#                 item.GlobalMenuClose()
#                 item.SetVisible(True)
#         else:
#             self.SetSelectedMenuItem(self.selectedNode.parent)
        
    def CheckPick(self, pickedActor):
        '''
        Checks what the user has picked
        '''
        
        # If the currently selected node is picked, do nothing
        if self.selectedNode.CheckActor(pickedActor):
            return
        
        # Check if any children were picked
        if self.CheckChildren(pickedActor) == True:
                return
        
        # Check if any parent items were picked    
        if self.CheckParent(self.selectedNode.parent, pickedActor) == True:
                return
        
#         if self.selectedNode == None:
#             for item in self.childrenObjects:
#                 if item.CheckActor(pickedActor) == True:
#                     self.__ActionMenuItem(item)
#                     return
            
    def CheckParent(self, parent, actor):
        '''
        Checks if any parent nodes were selected
        '''
        
        # Make sure we do not look at MenuItemController
        if type(parent) is not MenuItemController:
            
            if parent.CheckActor(actor) == True:
                # Perform action if selected node found
                self.__ActionMenuItem(parent)
                return True
            
            if type(parent.parent) is not MenuItemController:
                # Recurse until all parents have been checked.
                self.CheckParent(parent.parent, actor)
        
        # Return false if no parents selected        
        return False
        
    def CheckChildren(self, actor):
        '''
        Checks if any child nodes were selected
        '''
        
        # Check only the children of the currently selected node
        for child in self.selectedNode.childrenObjects:
            if type(child) is MenuItem.MenuItem:
                if child.CheckActor(actor) == True:
                    # Perform action if selected node found
                    self.__ActionMenuItem(child)
                    return True
                
        # Return false if no children selected
        return False
    
    def GetParentWidth(self, selectedNode):
        if type(selectedNode.parent) is MenuItemController:
            return selectedNode.GetWidth()
        else:
            return selectedNode.GetWidth() + self.GetParentWidth(selectedNode.parent)
        
    def GetChildHeight(self, selectedNode):
        for item in selectedNode.childrenObjects:
            if type(item) is MenuItem.MenuItem:
                if item.GetOpen():
                    return item.GetHeight() + self.GetChildHeight(item)
        else:
            return 0.0
        
    def GetRootParent(self, selectedNode):
        if type(selectedNode.parent) is MenuItemController:
            return selectedNode
        else:
            return self.GetRootParent(selectedNode.parent)
        
    def __ActionMenuItem(self, selectedNode):
        '''
        Action the menu item.
        '''
        self.selectedNode = selectedNode
        # If there are no children, close the menu (the callback has already been fired in MenuItem if it exists), otherwise expand it
        hasMenuChildren = False
        for item in selectedNode.childrenObjects:
            if type(item) is MenuItem.MenuItem:
                hasMenuChildren = True
                break
            
        if hasMenuChildren == True:
            for item in self.selectedNode.childrenObjects:
                if type(item) is MenuItem.MenuItem:
                    item.CloseMenuItem()
            self.selectedNode.OpenMenuItem()
            self.CloseUnselectedMenuItems()
            self.__SetAllParentPositions(self.selectedNode)
            self.__SetCurrentOptionsExpandedPosition(self.selectedNode)
        else: # Hit a leaf, close the global menu
            self.CloseMenu()

    def SetSelectedMenuItem(self, selectedNode):
        self.selectedNode = selectedNode
        if type(selectedNode.parent) is not MenuItemController:
            for item in self.childrenObjects:
                if item is not self.selectedNode:
                    #if type(item) is MenuItem:
                        item.SetVisible(False)
        for item in self.selectedNode.childrenObjects:
            if type(item) is MenuItem:
                item.CloseMenuItem()
        self.selectedNode.OpenMenuItem()
        self.CloseUnselectedMenuItems()
        self.SetMenuItemPositions(self.selectedNode)
        
#     def SetSelectedMenuItemLocation(self, selctedNodeLocation):
#         self.selectedNode.SetSelectedMenuItemLocation()

    def __SetCurrentOptionsExpandedPosition(self, selectedNode):
        '''
        I'm a bitch, I know.
        '''
        if len(selectedNode.childrenObjects) > 0:
            # Calculate the total height
            totalHeight = 0.0
            for item in selectedNode.childrenObjects:
                if type(item) is MenuItem.MenuItem:
                    totalHeight += item.GetHeight()
            # Find the vertical midpoint - the vertical origin for the children
            totalHeight = totalHeight / 2
            # Set all the children centered around this point
            for item in selectedNode.childrenObjects:
                if type(item) is MenuItem.MenuItem:
                    position = [(selectedNode.GetWidth() / 2) + (item.GetWidth() / 2), 0.0, 0.0]
                    position[0] += 0.0
                    position[1] = totalHeight - (item.GetHeight() / 2)
                    position[2] += 0.0
                    totalHeight -= item.GetHeight()
                    item.SetSceneObjectPosition(position)

    def __SetAllParentPositions(self, selectedNode):
        '''
        Put the current option at the origin (by moving the root node)
        '''
        # Special case - current node should be in the center
        totalWidth = 0
        # Traverse up the tree and calculate the total width of all the collapsed nodes
        rootMenuItem = selectedNode
        
        while type(selectedNode) is not MenuItemController:

            totalWidth += selectedNode.GetWidth() / 2

            validChild = None
            
            for item in selectedNode.childrenObjects:
                if type(item) is MenuItem.MenuItem:
                    validChild = item
                    break
            
            if validChild is not None:
                totalWidth += validChild.GetWidth() / 2
                
            #Make his (her?) vertical offset cero
            selectedNode.SetSceneObjectPosition([
                                                 (selectedNode.GetWidth() / 2) + (selectedNode.parent.GetWidth() / 2), 
                                                 0, #Force Y to zero.
                                                 0])
            selectedNode = selectedNode.parent
            # Keep track of the root node!
            if type(selectedNode) is not MenuItemController:
                rootMenuItem = selectedNode

        # Now set the child to the total width.
        rootMenuItem.SetSceneObjectPosition([-totalWidth,
                                             0,
                                             0
                                             ])
    
    def CloseUnselectedMenuItems(self):
        '''
        Close all unselected MenuItems
        '''
        # Find all unselected MeunItems
        for item in self.selectedNode.parent.childrenObjects:
            if item is not self.selectedNode:
                # Make sure we are closing a MenuItem
                if type(item) is MenuItem.MenuItem:
                    item.SetOpen(False)
                    item.SetVisible(False)
    
    def __BuildMenu(self):
        '''
        Build the main menu.
        '''

        mediaFolder = "../scene/media/menu/"
        
        rootTexs = 'root_node.png'
        
        # Get the textures
        rootSelectedTexs = [
                            '1high.png',
                            '2high.png',
                            '3high.png',
                            '4high.png'
                            ]
        rootUnselectedTexs = [
                            '1.png',
                            '2.png',
                            '3.png',
                            '4.png'
                            ]
        
        self.__pngRootReader = None
        self.__vtkRootTexs = None
        self.__pngRootUnselectedReaders = []
        self.__vtkRootUnselectedTexs = []
        self.__pngRootSelectedReaders = []
        self.__vtkRootSelectedTexs = []
        
        # Build root textures
        pngReaderRoot = vtk.vtkPNGReader()
        pngReaderRoot.SetFileName(mediaFolder + rootTexs)
        
        vtkTextureRoot = vtk.vtkTexture() 
        vtkTextureRoot.SetInputConnection(pngReaderRoot.GetOutputPort())
        vtkTextureRoot.InterpolateOn()
        vtkTextureRoot.RepeatOff()
        vtkTextureRoot.EdgeClampOn()
        
        self.__pngRootReader = pngReaderRoot
        self.__vtkRootTexs = vtkTextureRoot
        
        # Build the textures        
        for i in range(0,len(rootUnselectedTexs)):
            pngReader = vtk.vtkPNGReader()
            pngReader.SetFileName(mediaFolder + rootUnselectedTexs[i])
            
            vtkTexture = vtk.vtkTexture()
            vtkTexture.SetInputConnection(pngReader.GetOutputPort())
            vtkTexture.InterpolateOn()
            vtkTexture.RepeatOff()
            vtkTexture.EdgeClampOn()
            
            self.__pngRootUnselectedReaders.append(pngReader)
            self.__vtkRootUnselectedTexs.append(vtkTexture)
            
        for i in range(0,len(rootSelectedTexs)):
            pngReader = vtk.vtkPNGReader()
            pngReader.SetFileName(mediaFolder + rootSelectedTexs[i])
            
            vtkTexture = vtk.vtkTexture()
            vtkTexture.SetInputConnection(pngReader.GetOutputPort())
            vtkTexture.InterpolateOn()
            vtkTexture.RepeatOff()
            vtkTexture.EdgeClampOn()
            
            self.__pngRootSelectedReaders.append(pngReader)
            self.__vtkRootSelectedTexs.append(vtkTexture)
            
        leafSelectedTexs = [
                            '1optionhigh.png',
                            '2optionhigh.png',
                            '3optionhigh.png',
                            '4optionhigh.png'
                            ]
        leafUnselectedTexs = [
                            '1option.png',
                            '2option.png',
                            '3option.png',
                            '4option.png'
                            ]
        
        self.__pngleafUnselectedReaders = []
        self.__vtkleafUnselectedTexs = []
        self.__pngleafSelectedReaders = []
        self.__vtkleafSelectedTexs = []
        # Build the textures        
        for i in range(0,len(leafUnselectedTexs)):
            pngReader = vtk.vtkPNGReader()
            pngReader.SetFileName(mediaFolder + leafUnselectedTexs[i])
            
            vtkTexture = vtk.vtkTexture()
            vtkTexture.SetInputConnection(pngReader.GetOutputPort())
            vtkTexture.InterpolateOn()
            vtkTexture.RepeatOff()
            vtkTexture.EdgeClampOn()
            
            self.__pngleafUnselectedReaders.append(pngReader)
            self.__vtkleafUnselectedTexs.append(vtkTexture)
            
        for i in range(0,len(leafSelectedTexs)):
            pngReader = vtk.vtkPNGReader()
            pngReader.SetFileName(mediaFolder + leafSelectedTexs[i])
            
            vtkTexture = vtk.vtkTexture()
            vtkTexture.SetInputConnection(pngReader.GetOutputPort())
            vtkTexture.InterpolateOn()
            vtkTexture.RepeatOff()
            vtkTexture.EdgeClampOn()
            
            self.__pngleafSelectedReaders.append(pngReader)
            self.__vtkleafSelectedTexs.append(vtkTexture)
        
        self.__baseMenuItem = None
        
        rootMenuItems = []
        
        self.__baseMenuItem = MenuItem.MenuItem(self.__renderManager, 0.4 * 170/128, 0.4, self, "", self.__vtkRootTexs, self.__vtkRootTexs)
        # Now build the menu
        for i in range(0, 4):
            menuOption = MenuItem.MenuItem(self.__renderManager, 0.2, 0.2, self.__baseMenuItem, "", self.__vtkRootSelectedTexs[i], self.__vtkRootUnselectedTexs[i])
            rootMenuItems.append(menuOption)
        
        # Set the roles
        availableRoles = self.__roleManager.GetMenuItemsRolesAndCallbacks()
        availableBots = self.__botManager.GetMenuItemsBotsAndCallbacks()
        # If planner, get the available planners
        # If bots, get the list of bots
        
        for item in availableRoles:
            menuOption = MenuItem.MenuItem(self.__renderManager, 0.2*5.77, 0.2, rootMenuItems[0], item[0], self.__vtkleafSelectedTexs[0], self.__vtkleafUnselectedTexs[0], item[1], None)
            
        # Set the bots
        for item in availableBots:
            menuOption = MenuItem.MenuItem(self.__renderManager, 0.2*5.77, 0.2, rootMenuItems[1], item[0], self.__vtkleafSelectedTexs[1], self.__vtkleafUnselectedTexs[1])
        
        # Add exit options
        menuOption = MenuItem.MenuItem(self.__renderManager, 0.2*5.77, 0.2, rootMenuItems[3], "Shutdown ARNerve", self.__vtkleafSelectedTexs[1], self.__vtkleafUnselectedTexs[1], self.ExitARNerve, None)
        
            
    def ExitARNerve(self, object):
        '''
        Menu item callback for exiting.
        '''
        exit()
        