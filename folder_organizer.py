#!/usr/bin/python3
import os
import sys
import shutil
from constants import FILE_TYPES


def get_file_extension(file):
    extension = os.path.splitext(file)[1]
    extension_without_dot = extension.replace('.', '')
    return extension_without_dot


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
    print(sys.argv)
    if not sys.argv[1]:
        exit

    os.chdir(sys.argv[1])

    for item in os.listdir(os.getcwd()):
        if has_file_extension(item):
            extension = get_file_extension(item)
            MISSING_TYPES = []

            for dir_name, file_extensions in FILE_TYPES.items():
                if extension.upper() in file_extensions:
                    move_file_to_dir(item,  dir_name)
                else:
                    MISSING_TYPES.append(extension)
                    UNIQUE_MISSING_TYPES = list(set(MISSING_TYPES))

            LOGS = 'Logs'
            create_directory(LOGS)
            with open(os.path.join(LOGS, "organize.txt"), "a") as f:
                for missing_type in UNIQUE_MISSING_TYPES:
                    f.write(missing_type + "\n")
