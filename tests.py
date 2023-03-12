import os
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
        with open(file=self.filepath, mode='r', encoding='utf8') as file:
            for line in file.readlines():
                for char in line:
                    self.assertEqual(self.char, char)

    def test_delete_file_and_dir(self):
        test_path_dir = '/test'
        test_filepath = test_path_dir + '/test_file.txt'
        os.mkdir(test_path_dir)
        file = open(test_filepath, "w+", encoding='utf8')
        file.close()
        self.assertTrue(os.path.isdir(test_path_dir))
        self.assertTrue(os.path.isfile(test_filepath))
        file_result = self.cleaner.delete_object(test_filepath)
        dir_result = self.cleaner.delete_object(test_path_dir)
        self.assertTrue(file_result)
        self.assertTrue(dir_result)


if __name__ == '__main__':
    unittest.main()
