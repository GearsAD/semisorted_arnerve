'''
Created on Nov 12, 2014

@author: alucard
'''

import vtk

from SceneObject import SceneObject
from scene import MenuItem

class MenuItemController(SceneObject):
    
    def __init__(self, renderers, iren, menuName):
        
        super(MenuItemController, self).__init__(renderers)
        
        self.renderers = renderers
        
        #super(MenuItemController, self).__init__(renderer)
        
        self.__pickerHandle = iren.AddObserver("EndPickEvent", self._OnPickEvent)
        
        self.name = menuName
        
        self.menuItemList = []
        
        #self.root = MenuItem(renderer, 2, 4, 3, None, name)
        #self.selectedNode = self.root
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
    
    #def GetParent(self):
        #return self.root
    
    def SetOpen(self, state):
        self.isOpen = state
        
    def AddMenuItem(self, newMenuItem):
        self.menuItemList.append(newMenuItem)
        self.childrenObjects.append(newMenuItem)
    
    def OpenMenu(self):
        self.SetOpen(True)
        self.SetMenuItemControllerMenuItemLocation()
        for item in self.menuItemList:
            item.SetVisible(True)
        #self.selectedNode = self.root
        #self.selectedNode.OpenMenuItem()
        #self.SetSelectedMenuItem(self.selectedNode)
        
    def CloseMenu(self):
        self.SetOpen(False)
        for item in self.menuItemList:
            item.GlobalMenuClose()
        #self.root.GlobalMenuClose()
        
    def CloseCurrentMenuItem(self):
        if self.selectedNode.parent == None:
            self.selectedNode = None
            self.SetMenuItemControllerMenuItemLocation()
            for item in self.menuItemList:
                item.GlobalMenuClose()
                item.SetVisible(True)
        else:
            self.SetSelectedMenuItem(self.selectedNode.parent)
        
    def CheckPick(self, pickedActor):
        if self.selectedNode == None:
            for item in self.menuItemList:
                if item.CheckActor(pickedActor) == True:
                    self.SetSelectedMenuItem(item)
        if self.CheckChildren(pickedActor) == True:
            return
        if self.CheckParent(self.selectedNode.parent, pickedActor) == True:
            return
        
    def CheckParent(self, parent, actor):
        if parent is not None:
            if parent.CheckActor(actor) == True:
                self.SetSelectedMenuItem(parent)
                return True
            if parent.parent is not None:
                self.CheckParent(parent.parent, actor)
        return False
        
    def CheckChildren(self, actor):
        for item in self.selectedNode.childMenuItems:
            if item.CheckActor(actor) == True:
                self.SetSelectedMenuItem(item)
                return True
        return False
    
    def SetMenuItemControllerMenuItemLocation(self):
        if len(self.menuItemList) > 0:
            totalHeight = 0.0
            for item in self.menuItemList:
                totalHeight += item.GetHeight()
            totalHeight = totalHeight / 2
            for item in self.menuItemList:
                position = [0.0, 0.0, 0.0]
                position[0] = 0.0
                position[1] = totalHeight - (item.GetHeight() / 2)
                position[2] = item.GetDepth()
                totalHeight -= item.GetHeight()
                item.SetPosition(position)
            
    def SetSelectedMenuItem(self, selectedNode):
        self.selectedNode = selectedNode
        if self.selectedNode.parent is None:
            for item in self.menuItemList:
                if item is not self.selectedNode:
                    item.SetVisible(False)
        for item in self.selectedNode.childMenuItems:
            item.CloseMenuItem()
        self.selectedNode.OpenMenuItem()
        self.selectedNode.CloseUnselectedMenuItems()
        self.selectedNode.SetParentMenuItemPositions([0.0, 0.0, 0.0])
        self.selectedNode.SetChildMenuItemPositions()
        #if len(self.selectedNode.GetChildCount) <= 0:
        
    def SetSelectedMenuItemLocation(self, selctedNodeLocation):
        self.selectedNode.SetSelectedMenuItemLocation()
            #self.CloseMenu()
    def BuildTestMenu(self):
        MenuOption01 = MenuItem.MenuItem(self.renderers, 0, 4, 3, None, "Option 01", "")
        MenuOption02 = MenuItem.MenuItem(self.renderers, 0, 4, 3, None, "Option 02", "")
            
        MenuOption03 = MenuItem.MenuItem(self.renderers, 0, 4, 3, MenuOption02, "Option 02/01", "")
        MenuOption04 = MenuItem.MenuItem(self.renderers, 0, 4, 3, MenuOption02, "Option 02/02", "")
        MenuOption05 = MenuItem.MenuItem(self.renderers, 0, 4, 3, MenuOption02, "Option 02/03", "")
            
        MenuOption06 = MenuItem.MenuItem(self.renderers, 0, 4, 3, MenuOption05, "Option 05/01", "")
        MenuOption07 = MenuItem.MenuItem(self.renderers, 0, 4, 3, MenuOption05, "Option 05/02", "")
        
        self.AddMenuItem(MenuOption01)
        self.AddMenuItem(MenuOption02)
        
        self.OpenMenu()
        