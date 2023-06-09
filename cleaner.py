import os
import shutil


class Cleaner:
    @staticmethod
    def fill_file(path: str, char: str = 'r', offset: int = 3) -> bool:
        if os.path.isfile(path):
            with open(file=path, mode='r', encoding='utf8') as file:
                lines = file.readlines()
            with open(file=path, mode='w', encoding='utf8') as file:
                for line in lines:
                    count_of_chars = len(line)
                    file.write(str(char * count_of_chars * offset) + '\n')
            return True
        return False

    @staticmethod
    def delete_object(path: str) -> bool:
        """ Удаление файла или директории с файлами """

        if os.path.isfile(path):
            os.remove(path)
            return True
        elif os.path.isdir(path):
            shutil.rmtree(path)
            return True
        return False

    @staticmethod
    def full_delete_dir(dir_name: str) -> bool:
        """ Рекурсивная очистка и удаления файлов и подкаталогов"""

        def recursive_deletion(dir_name: str):
            for root, dirs, files in os.walk(dir_name):
                print(f'Директория - {root}:')
                for file in files:
                    print(f'Удаление файла {file}...')
                    file_path = f'{root}\\{file}'
                    assert Cleaner.fill_file(path=file_path)
                    assert Cleaner.delete_object(path=file_path)
            Cleaner.delete_object(path=f'{dir_name}')
        if os.path.isdir(dir_name):
            recursive_deletion(dir_name)
            return True
        return False

    @staticmethod
    def full_delete_file(file_name: str) -> bool:
        """ Полное удаление файла """

        if not os.path.isfile(file_name):
            return False
        assert Cleaner.fill_file(path=file_name)
        assert Cleaner.delete_object(path=file_name)
        return True


if __name__ == '__main__':
    # Cleaner.fill_file('dir_with_data/file_with_data.txt')
    # Cleaner.full_delete_dir(dir_name='dir_with_data')
    Cleaner.full_delete_file(file_name='dir_with_data/file1.txt')
