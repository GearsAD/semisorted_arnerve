'''
Created on Dec 3, 2014

@author: gearsad
'''
import sys
from roverpylot import rover
from bot_update_t import bot_update_t
from bot_control_command_t import bot_control_command_t
import lcm

# Try to start OpenCV for video
try:
    import cv
except:
    cv = None



class LCMRover(rover.Rover):
    '''
    A rover using LCM for control and camera feed upstream
    '''
                
    def Initialize(self, botname):
        '''
        Init the rover and store the name
        '''        
        self.__botname = botname
        
        self.__lcm = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
        
        self.__controlSubscription = self.__lcm.subscribe("ARNerve_Bot_Control_" + self.__botname, self.UpdateBotControlHandler)
        
        self.__lightsOn = 0
        self.__infraredOn = 0
            
    def processVideo(self, jpegbytes):
                            
        #try:
            
            camUpdate = bot_update_t()
            camUpdate.name = self.__botname
            camUpdate.numBytes_cameraFrameJpeg = len(jpegbytes)
            camUpdate.cameraFrameJpeg = jpegbytes
            # Get the battery health as well
            battery = self.getBatteryPercentage()
            camUpdate.batteryPercentage = battery
            
            self.__lcm.publish("ARNerve_Bot_Update_" + self.__botname, camUpdate.encode())
            
        #except:
        #    print "Exception", sys.exc_info()[0]
        #    pass
    
    def Update(self):
        '''
        Update the LCM
        '''
        self.__lcm.handle()
        
    def Disconnect(self):
        self.lc.unsubscribe(self.__controlSubscription)
        
    def UpdateBotControlHandler(self, channel, data):
        '''
        Get the updated bot parameters and send them to the bot.
        '''
        controlParams = bot_control_command_t.decode(data)
        
        # Check if it is the right bot.
        if self.__botname != controlParams.name:
            return 
        
        self.setTreads(controlParams.botTreadVelLeft, controlParams.botTreadVelright)
        print "Setting the treads to {0}, {1}".format(controlParams.botTreadVelLeft, controlParams.botTreadVelright)
        if self.__lightsOn != controlParams.isLightsOn:
            if controlParams.isLightsOn != 0:
                self.turnLightsOn()
            else:
                self.turnLightsOff()
            self.__lightsOn = controlParams.isLightsOn
        if self.__infraredOn != controlParams.isInfraredOn:
            if controlParams.isInfraredOn != 0:
                self.turnInfraredOn()
            else:
                self.turnInfraredOff()
            self.__infraredOn = controlParams.isInfraredOn
            