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
        self.new_user.save_contact()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


if __name__ == '__main__':
    unittest.main()