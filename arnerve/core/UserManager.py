'''
Created on Nov 22, 2014

@author: gearsad
'''
from user_update_t import user_update_t
from kinect_update_t import kinect_update_t, kinect_joint_t
from oculus_update_t import oculus_update_t
from wearable_update_t import wearable_update_t
from scene import User

class UserManager(object):
    '''
    A manager for all the users in the scene (populated by LCM, consumed everywhere :)) 
    '''

    def __init__(self, thisUserName):
        '''
        Constructor
        '''
        self.__thisUserName = thisUserName
             
        self.currentUser = user_update_t()
        # Initialize him/her until LCM updates it.
        self.currentUser.kinect = kinect_update_t()
        self.currentUser.kinect.headposition = kinect_joint_t.kinect_joint_t()
        self.currentUser.kinect.torsoposition = kinect_joint_t.kinect_joint_t()
        self.currentUser.oculus = oculus_update_t()
        print "HACK - populate a full user UserManager __init__ if you are planning on using it in the future."
        
    def Attach(self, botManager, roleManager, renderManager):
        '''
        Attach the managers to the UserManager
        '''
        self.__renderManager = renderManager
        self.__botManager = botManager
        self.__roleManager = roleManager
        
        # Create the other users.
        self.users = []
        
        self.currentUserModel = User.User(self.__botManager, self.__roleManager, self.__renderManager, self.__thisUserName)
        self.otherUserModels = []
        
    def UpdateUser(self, user):
        '''
        Method to update the users list with a new or current user.
        '''
        if(user.name == self.__thisUserName):
            self.currentUser = user
            self.currentUserModel.UpdateUser(self.currentUser)
            print "Oculus Orientation for {0} = {1}, {2}, {3}".format(user.name, user.oculus.headorientation[0],user.oculus.headorientation[1], user.oculus.headorientation[2])
        else:
            #Update the other users
            found = False
            index = 0
            for myUser in self.users:
                if(myUser.name == user.name): #Update this user
                    self.users[index] = user #Replace the user, we found it
                    self.otherUserModels[index].UpdateUser(user)
                    found = True
                else:
                    index = index + 1
            if(found is not True):
#                 newUser = User.User(self.__renderers, user.name)
                print "Adding another user - moving him away from the axis! Remove in future."
#                 newUser.vtkActor.SetPosition([0, 0, 10])
                print "[UserManager.py] Ignoring the other user for now."
#                 self.users.append(user)
#                 self.otherUserModels.append(newUser)

    def GetCurrentUser(self):
        return self.__thisUserName