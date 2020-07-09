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
    if not sys.argv[1]:
        exit

    os.chdir(sys.argv[1])
    CURRENT_WORKING_DIR = os.getcwd()

    for item in os.listdir(CURRENT_WORKING_DIR):
        if has_file_extension(item):
            extension = get_file_extension(item)

            for dir_name, file_extensions in FILE_TYPES.items():
                if extension.upper() in file_extensions:
                    move_file_to_dir(item,  dir_name)

                else:
                    create_directory(dir_name)
                    file_path = os.path.join(dir_name, "organize.log")

                    with open(file_path, "a") as f:
                        f.write(extension + "\n")
