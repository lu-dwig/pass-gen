#!/usr/bin/env python3.9
import random
import string
# import pyperlip
class User:
    """
    create User class that generates new instances of a user.
    
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
 
 
class Credentials():
    """
    Create credentials class to help create new objects of credentials 
    """ 
    credentials_list =[]
    @classmethod
    def verify_user(cls,username,password):
        """
        method to very whether the user is in our user_list or not 
        """     
        a_user = ""
        for user in User.user_list:
            if (user.username ==username and user.password == password):
                    a_user == user.username
        return a_user
    
    def __init__(self,account,userName,password):
        """
        method that defines user credientials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store new credentials to the credentials list 
        """
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        """
        delete credentials method that deletes an account from the credentials list
        """
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_credentials(cls,account):
        """
        method that takes in an account_name and returns the credentials that matches that account_name.
        """
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials
            
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credentials(account)
        # pyperclip.copy(found_credentials.password)
        
    @classmethod
    def if_credentials_exist(cls, account):
        """
        method that checks if a credential exists from the credentials list and returns true or false depending if the credential exists.
        """
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list

    def generatePassword(stringLength=8):
        """
        Generate a random password string of letters and digits and special characters
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))          