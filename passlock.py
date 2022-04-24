import random
import string
# import pyperlip
class User:
    """
    cretae User class that generates new instances of a user.
    
    """
    user_list = []
    
    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username 
        self.password = password
    
    def save_user(self):
        """
        A method that saves a new user instance into the user list
        """
        User.user_list.append(self)
       
    @classmethod
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        '''
        delete_account method deltes a saved account from the list of users
        '''    
        User.user_list.remove(self)
        