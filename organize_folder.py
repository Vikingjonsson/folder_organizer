#!/usr/bin/python3
import os
import sys
import shutil


def get_file_extension(file: str) -> str:
    return os.path.splitext(file)[1]


def has_file_extension(file):
    return get_file_extension(file) != ''


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def move_file_to_dir(file_path, dir_path):
    create_directory(dir_path)
    dest = os.path.join(dir_path, file_path)
    shutil.move(file_path, dest)


if __name__ == '__main__':
    if not sys.argv[1]:
        exit

    os.chdir(sys.argv[1])
    CURRENT_WORKING_DIR = os.getcwd()

    FOLDER_PATHS = {
        'Start': os.path.join(CURRENT_WORKING_DIR, 'Texts'),
        'MOV': os.path.join(CURRENT_WORKING_DIR, 'Movies'),
        'IMG': os.path.join(CURRENT_WORKING_DIR, 'Images'),
        'PDF': os.path.join(CURRENT_WORKING_DIR, 'PDFs'),
        'LOG': os.path.join(CURRENT_WORKING_DIR, 'Logs')
    }

    FILE_TYPES = {
        'MOV': '[.mov]',
        'TXT': '[.txt]',
        'IMG': ['.jpeg', '.jpg', '.png'],
        'PDF': '[.pdf]',
        'LOG': '[.log]'
    }

    for item in os.listdir(CURRENT_WORKING_DIR):
        if has_file_extension(item):
            extension = get_file_extension(item)
            item_path = os.path.join(CURRENT_WORKING_DIR, item)

            for key, value in FILE_TYPES.items():
                print('key: ', key)
                print(value)

            if extension in FILE_TYPES['MOV']:
                move_file_to_dir(item_path, FOLDER_PATHS['MOV'])

            elif extension in FILE_TYPES['PDF']:
                move_file_to_dir(item_path, FOLDER_PATHS['PDF'])

            elif extension in FILE_TYPES['TXT']:
                move_file_to_dir(item_path, FOLDER_PATHS['TEXT'])

            elif extension in FILE_TYPES['IMG']:
                move_file_to_dir(item_path, FOLDER_PATHS['IMG'])

            else:
                create_directory(FOLDER_PATHS['LOG'])
                file_name = os.path.join(
                    FOLDER_PATHS['LOGS'], "missing_extensions.log")

                with open(file_name, "a") as f:
                    f.write(extension + "\n")
