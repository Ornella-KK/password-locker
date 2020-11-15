import unittest
import user from User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Ornella")#create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Ornella")