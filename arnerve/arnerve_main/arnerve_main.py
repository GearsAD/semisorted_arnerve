'''
Created on Nov 20, 2014

@author: gearsad
'''

import sys

from scene import InteractorMapUser
from scene import Interactor1stPersonUser
from scene import Interactor3rdPerson

from core import WorldManager

if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print "Run arneve with the following paramaters - name, type, width, height"
        sys.exit()
    
    name = sys.argv[1]
    device = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    
    worldManager = WorldManager.WorldManager(name, device, width, height)
        
    worldManager.Start()
    pass