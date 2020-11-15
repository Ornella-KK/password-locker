import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("4556")

    def test_init(self):
        self.assertEqual(self.new_credential.password,"4556")

    def test_save_contact(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        Credential.credential_list = []

    def test_save_multiple_contact(self):
        self.new_credential.save_credential()
        test_credential = Credential("4556")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
if __name__ == '__main__':
    unittest.main()