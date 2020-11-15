import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential(4556)

    def test_init(self):
        self.assertEqual(self.new_credential.password,"4556")