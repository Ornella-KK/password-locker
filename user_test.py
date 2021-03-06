import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Ornella")#create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Ornella")
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
        self.new_user.save_user()
        test_user = User("user")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
            test_delete_user to test if we can remove a user from our user list
            '''
        self.new_user.save_user()
        test_user = User("user")
        test_user.save_user()

        self.new_user.delete_user() #deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("user")
        test_user.save_user()

        user_exists = User.user_exist("Ornella")
        self.assertTrue(user_exists)

    def test_display_all_user(self):
         '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_user(),User.user_list)


if __name__ == '__main__':
    unittest.main()