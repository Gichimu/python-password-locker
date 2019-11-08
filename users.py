

class Users:
    '''
    Class that defines the attributes and behaviour for a user
    '''
    users = []

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password


    def save_user(self):
        '''
        Save a user's credentials on registering
        '''

        Users.users.append(self)

    def delete_user(self):
        '''
        Remove user from the users list
        '''

        Users.users.remove(self)
    

    @classmethod
    def user_exists(cls, username):
        '''
        Check if a user exists

        Args:
            username: username of the user account to check
        '''

        found_user = find_user(username)
        if(found_user):
            return True
        else:
            return False


    @classmethod
    def find_user(cls, username):
        '''
        Find a user using their username

        Args:
            username: username of the account to look for

        return:
            the found user
        '''
        for user in cls.users:
            if(user.username == username):
                return user

    @classmethod
    def show_all(cls):
        '''
        Returns all the available contacts
        '''

        return cls.users



            




