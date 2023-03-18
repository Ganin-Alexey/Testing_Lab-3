import os
import shutil
import unittest
from cleaner import Cleaner


class CleanerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cleaner = Cleaner()
        cls.filepath = 'dir_with_data/1.txt'
        cls.dir_path = 'dir_with_data/{0}'
        cls.char = 'g'

    def create_file(self, name: str = 'default', path: str = 'dir_with_data/'):
        file = open(f'{path}/{name}.txt', "w", encoding='utf8')
        file.close()

    def setUp(self):
        os.mkdir(self.dir_path.format(''))
        os.mkdir(self.dir_path.format('dir1'))
        os.mkdir(self.dir_path.format('dir2'))
        os.mkdir(self.dir_path.format('dir2/dir3'))
        os.mkdir(self.dir_path.format('empty_directory'))
        self.create_file(name='1', path=self.dir_path.format(''))
        self.create_file(name='2', path=self.dir_path.format(''))
        self.create_file(name='3', path=self.dir_path.format(''))
        self.create_file(name='4', path=self.dir_path.format('dir1'))
        self.create_file(name='5', path=self.dir_path.format('dir1'))
        self.create_file(name='6', path=self.dir_path.format('dir2/dir3'))
        self.create_file(name='7', path=self.dir_path.format('dir2/dir3'))

    def tearDown(self):
        if os.path.exists(self.dir_path.format('')):
            shutil.rmtree(self.dir_path.format(''))

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
        self.assertTrue(os.path.isdir(self.dir_path.format('')))
        self.assertTrue(os.path.isfile(self.filepath))
        file_result = self.cleaner.delete_object(self.filepath)
        dir_result = self.cleaner.delete_object(self.dir_path.format('empty_directory'))
        self.assertTrue(file_result)
        self.assertTrue(dir_result)

    def test_full_delete_dir(self):
        result = self.cleaner.full_delete_dir(dir_name=self.dir_path.format(''))
        self.assertTrue(result)

    def test_full_delete_file(self):
        result = self.cleaner.full_delete_file(file_name=self.filepath)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
