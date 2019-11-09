import unittest
from users import Users
from credentials import Credentials


class testAccounts(unittest.TestCase):
    '''
    Test Class for performing tests on different user and credentials functionality
    '''

    def setUp(self):
        '''
        Setting up the initial objects for the tests
        '''

        self.new_user = Users("Mike", "Omondi", "mike@user.com", "mikeOmondi", "mikeomondi1234")
        self.new_credential = Credentials("facebook", "kamau1", "12345kamau1")


    def tearDown(self):
        '''
        Cleaning up the users and credentials lists after each test run
        '''

        Users.users = []
        Credentials.credentials = []


    #######################################
                #user tests
    #######################################


    def test_initUser(self):
        '''
        Test to see if the users object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Mike")
        self.assertEqual(self.new_user.last_name, "Omondi")
        self.assertEqual(self.new_user.email, "mike@user.com")
        self.assertEqual(self.new_user.username, "mikeOmondi")
        self.assertEqual(self.new_user.password, "mikeomondi1234")


    def test_find_user(self):
        '''
        Test to see if the a user can search for an account using a username
        '''
        self.new_user.save_user()
        new_user = Users("user1", "test", "test@user.com", "usr1", "pass")
        new_user.save_user()
        user_found = Users.find_user('usr1')

        self.assertEqual(user_found.email, new_user.email)


    def test_del_user(self):
        '''
        Test to check if a user can delete a user account
        '''
        self.new_user.save_user()
        test_user = Users("user", "test", "user@test.com", "usr", "user123")
        test_user.save_user()

        Users.delete_user(test_user)

        self.assertEqual(len(Users.users), 1)

    def test_create_user(self):
        '''
        Test to see if a user can be created
        '''

        test_user = Users("user", "test", "user@test.com", "usr", "user123")
        test_user.save_user()

        found_user = Users.find_user("usr")

        self.assertEqual(found_user.email, test_user.email)

    def test_show_all(self):

        '''
        Test to see if a user can see all accounts
        '''
        
        self.assertEqual(Users.users, Users.show_all())


#######################################################
            #Credentials Tests
#######################################################

    def test_init_credentials(self):
        '''
        Test if the credentials property is initialized propertly
        '''

        self.assertEqual(self.new_credential.account_name, "facebook")
        self.assertEqual(self.new_credential.username, "kamau1")
        self.assertEqual(self.new_credential.password, "12345kamau1")


    def test_save_credential(self):
        '''
        Test if a credential can be saved in the credentials list
        '''

        test_credential = Credentials("test", "username", "password")
        test_credential.save_credential()

        self.assertEqual(len(Credentials.credentials), 1)

    def test_save_multiple_credentials(self):
        '''
        Test if multiple credentials can be saved in the credentials list
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("test", "username", "password")
        test_credential.save_credential()
        test_credential1 = Credentials("test1", "username1", "password1")
        test_credential1.save_credential()

        self.assertEqual(len(Credentials.credentials), 3)


    def test_del_credential(self):
        '''
        Test to see if a credential can be removed from the credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("test", "username", "password")
        test_credential.save_credential()

        Credentials.delete_credential(test_credential)
        self.assertEqual(len(Credentials.credentials), 1)

    def test_find_by_password(self):
        '''
        Test if a credential can be searched for using the password
        '''

        self.new_credential.save_credential()
        found_credential = Credentials.find_by_password("12345kamau1")

        self.assertEqual(found_credential.username, self.new_credential.username)



if __name__ == '__main__':
    unittest.main()