import unittest
from cleaner import Cleaner


class CleanerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    # def tearDownClass(self):
    #     pass

    def setUp(self):
        pass

    def test_create_class(self):
        cleaner = Cleaner()
        self.assertIsInstance(cleaner, Cleaner)


if __name__ == '__main__':
    unittest.main()
