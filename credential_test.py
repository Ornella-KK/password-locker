import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("4556")

    def test_init(self):
         '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.password,"4556")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential list
            '''
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
        
    def test_delete_credential(self):
         '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("4556")
        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
         '''
        method that returns a list of all credential saved
        '''
        self.assertEqual(Credential.display_credential(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()