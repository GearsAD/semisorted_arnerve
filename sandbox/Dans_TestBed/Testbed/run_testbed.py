'''
Created on Aug 5, 2014

@author: gearsad
'''
# To allow the project to be run from outside Eclipse PyDev
import sys
sys.path.append('../')

import vtk

from MenuItem import MenuItem
from MenuItemController import MenuItemController

# Cheap test viewmodel
class MenuViewModel():
    def __init__(self):
        i = 0
    
    def Button1Pressed(self, target):
        print "BUTTON PRESSED!"

if __name__ == '__main__':
    
    # A renderer and render window
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    
    # Make it a little bigger than default
    renderWindow.SetSize(1280, 480)
    
    #renderWindow.HideCursor()
    
    renderWindow.StereoCapableWindowOn()
    renderWindow.SetStereoTypeToSplitViewportHorizontal()
    
    #activates stereo by default. Press '3' to toggle stereo
    renderWindow.StereoRenderOn()
    
    #may need to use to alter eye angle
    #renderer.GetActiveCamera().SetEyeAngle(number)

    # An interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    
    #Create a sphere
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(5)
 
    #Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphereSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    renderer.AddActor(actor)
    #renderer.Camera.SetEyeAngle(65)
    #renderer.ResetCamera()
    
    #Menu = MenuItemController(renderer, renderWindowInteractor, "UserMenu")
    
    #testModel = MenuViewModel()
    
    #MenuOption01 = MenuItem(renderer, 0, 4, 3, None, "Option 01", "", testModel, testModel.Button1Pressed)
    #MenuOption02 = MenuItem(renderer, 0, 4, 3, None, "Option 02", "")
    
    #MenuOption03 = MenuItem(renderer, 0, 4, 3, MenuOption02, "Option 02/01", "")
    #MenuOption04 = MenuItem(renderer, 0, 4, 3, MenuOption02, "Option 02/02", "")
    #MenuOption05 = MenuItem(renderer, 0, 4, 3, MenuOption02, "Option 02/03", "")
    
    #MenuOption06 = MenuItem(renderer, 0, 4, 3, MenuOption05, "Option 05/01", "")
    #MenuOption07 = MenuItem(renderer, 0, 4, 3, MenuOption05, "Option 05/02", "")
    
    #Menu.AddMenuItem(MenuOption01)
    #Menu.AddMenuItem(MenuOption02)
    
    #print(Menu)
    #print(Menu.GetParent())
    #print(MenuOption01)
    #print(MenuOption02)
    
    #Menu.OpenMenu()
    
    #Menu.SetSelectedMenuItem(MenuOption02)
    
    #print(Menu)
    #print(MenuOption01)
    #print(MenuOption02)
    #print(MenuOption03)
    #print(MenuOption04)
    
    #Menu.CloseMenu()
    
    #print(Menu)
    #print(Menu.GetParent())
    #print(MenuOption01)
    #print(MenuOption02)
    
    # Render an image (lights and cameras are created automatically)
    renderWindow.Render()
    
    # Begin mouse interaction
    renderWindowInteractor.Start()
    renderWindowInteractor.Initialize()

    pass
