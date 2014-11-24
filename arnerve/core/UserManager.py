'''
Created on Nov 22, 2014

@author: gearsad
'''
from user_update_t import user_update_t
from scene import User

class UserManager(object):
    '''
    A manager for all the users in the scene (populated by LCM, consumed everywhere :)) 
    '''

    def __init__(self, renderers, thisUserName):
        '''
        Constructor
        '''
        
        self.__thisUserName = thisUserName
        self.__renderers = renderers; 
        
        self.currentUser = user_update_t()
        self.users = []
        
        self.currentUserModel = User.User(renderers, thisUserName)
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
                self.users.append(user)
                self.otherUserModels.append(User.User(self.__renderers, user.name))
                
                
                
                
                
                
                