import unittest # Importing the unittest module
from user import User #importing the user class
from credentials import Credentials #importing the credentials class

class TestUser(unittest.TestCase):
    """test case to test user methods"""
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Vector254","123123") # create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []    
         
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Vector254")
        self.assertEqual(self.new_user.password,"123123")
  
    def test_save_login(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_login() # saving the new user
        self.assertEqual(len(User.user_list),1)



class TestCredentials(unittest.TestCase):
    """test case to test credentials methods"""
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","Vector254","123123") # create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Twitter")
        self.assertEqual(self.new_credentials.username,"Vector254")
        self.assertEqual(self.new_credentials.password,"123123")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the user list
        '''
        self.new_credentials.save_credential() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credentials.save_credential()
            test_credential = Credentials("Twitter","Vector254","123123") # new contact
            test_credential.save_credential()

            self.new_credentials.del_account()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()

