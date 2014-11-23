'''
Created on Nov 22, 2014

@author: gearsad
'''
from user_update_t import user_update_t


class UserViewModel(object):
    '''
    A viewmodel for all the users in the scene (populated by LCM, consumed everywhere :)) 
    '''

    def __init__(self, thisUserName):
        '''
        Constructor
        '''
        
        self.__thisUserName = thisUserName 
        
        self.currentUser = user_update_t()
        self.users = []
        
    def UpdateUser(self, user):
        '''
        Method to update the users list with a new or current user.
        '''
        if(user.name == self.__thisUserName):
            self.currentUser = user
        else:
            #Update the other users
            found = False
            index = 0
            for myUser in self.users:
                if(myUser.name == user.name): #Update this user
                    self.users[index] = user #Replace the user, we found it
                    found = True
                else:
                    index = index + 1
            if(found is not True):
                self.users.append(user)