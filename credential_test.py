import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("4556")

    def test_init(self):
        self.assertEqual(self.new_credential.password,"4556")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
        
    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()

        credential_exists = Credential.credential_list("4556")
        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        self.assertEqual(Credential.display_credential(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()