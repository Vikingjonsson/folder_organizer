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


def move_file_to_dir(file_name, dir_path):
    cwd = os.getcwd()
    create_directory(dir_path)
    src = os.path.join(cwd, file_name)
    dest = os.path.join(cwd, dir_path, file_name)
    shutil.move(src, dest)


if __name__ == '__main__':
    if not sys.argv[1]:
        exit

    os.chdir(sys.argv[1])
    CURRENT_WORKING_DIR = os.getcwd()

    FOLDER_PATHS = {
        'TXT': 'Texts',
        'MOV': 'Movies',
        'IMG': 'Images',
        'PDF': 'PDFs',
        'LOG': 'Logs',
        'IMG': 'Disk images'
    }

    FILE_TYPES = {
        'MOV': ['.mov'],
        'TXT': ['.txt'],
        'IMG': ['.jpeg', '.jpg', '.png'],
        'PDF': ['.pdf'],
        'LOG': ['.log'],
        'IMG': ['.img']
    }

    for item in os.listdir(CURRENT_WORKING_DIR):
        if has_file_extension(item):
            extension = get_file_extension(item)

            for key, values in FILE_TYPES.items():
                print(extension in values)
                if extension in values:
                    move_file_to_dir(item, FOLDER_PATHS[key])

            else:
                create_directory(FOLDER_PATHS['LOG'])
                file_path = os.path.join(FOLDER_PATHS['LOG'], "organize.log")

                with open(file_path, "a") as f:
                    f.write(extension + "\n")
