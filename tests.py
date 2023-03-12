import unittest
from cleaner import Cleaner


class CleanerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cleaner = Cleaner()
        cls.filepath = 'dir_with_data/file_with_data.txt'
        cls.dir_path = 'dir_with_data/'
        cls.char = 'g'

    # def tearDownClass(self):
    #     pass

    def setUp(self):
        pass

    def test_create_class(self):
        self.assertIsInstance(self.cleaner, Cleaner)

    def test_fill_file(self):
        result = self.cleaner.fill_file(path=self.filepath, char=self.char)
        self.assertTrue(result)
        with open(file=self.filepath, mode='r') as file:
            for line in file.readlines():
                for char in line:
                    self.assertEqual(self.char, char)


if __name__ == '__main__':
    unittest.main()
