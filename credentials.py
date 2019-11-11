
import pyperclip
class Credentials:
    '''
    Class that defines attributes and default behaviour for the credentials class
    '''
    credentials = []

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

    
    def save_credential(self):
        '''
        Saving the credential in the credentials list
        '''
        
        Credentials.credentials.append(self)


    def delete_credential(self):
        '''
        Removing the credential fro the credentials list
        '''

        Credentials.credentials.remove(self)

    @classmethod
    def find_by_password(cls, password):
        '''
        check to see if an account is present in the credentials list

        Args:
            password: the password of the contact to be checked

        Return:
            returns the account if found or null if not found
        '''

        for credential in cls.credentials:
            if(credential.password == password):
                return credential

    @classmethod
    def display_all(cls):
        '''
        Displays all contacts saved
        '''

        return cls.credentials
