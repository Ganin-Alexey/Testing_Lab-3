import os
import shutil


class Cleaner:
    @staticmethod
    def fill_file(path: str, char: str = 'r', offset: int = 3) -> bool:
        if os.path.isfile(path):
            with open(file=path, mode='w+', encoding='utf8') as file:
                for line in file.readlines():
                    count_of_chars = len(line)
                    print(char, count_of_chars, offset)
                    print(char * count_of_chars * offset)
                    file.write(str(char * count_of_chars * offset))
            return True
        return False

    @staticmethod
    def delete_object(path: str) -> bool:
        if os.path.isfile(path):
            os.remove(path)
            return True
        elif os.path.isdir(path):
            shutil.rmtree(path)
            return True
        return False


if __name__ == '__main__':
    pass