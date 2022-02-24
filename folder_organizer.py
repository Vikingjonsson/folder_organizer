#!/usr/bin/python3
import os
import sys
import shutil
from os import listdir, chdir, getcwd, makedirs
from os.path import isfile, join, exists, splitext
from constants import FILE_TYPES


def get_file_extension(file):
    extension = splitext(file)[1]
    extension_without_dot = extension.replace('.', '')
    return extension_without_dot


def has_file_extension(file):
    return get_file_extension(file) != ''


def create_directory(directory_name):
    if not exists(directory_name):
        makedirs(directory_name)


def move_file_to_dir(file_name, dir_path):
    cwd = getcwd()
    create_directory(dir_path)
    src = join(cwd, file_name)
    dest = join(cwd, dir_path, file_name)
    shutil.move(src, dest)


if __name__ == '__main__':
    print(sys.argv)
    DIRECTORY_PATH = sys.argv[1]

    if not DIRECTORY_PATH:
        exit

    chdir(DIRECTORY_PATH)

    UNIQUE_MISSING_TYPES = []
    MISSING_TYPES = []
    ALL_FILES_IN_DIRECTORY = [f for f in listdir(
        DIRECTORY_PATH) if isfile(join(DIRECTORY_PATH, f))]

    for item in ALL_FILES_IN_DIRECTORY:
        if has_file_extension(item):
            extension = get_file_extension(item)

            for dir_name, file_extensions in FILE_TYPES.items():
                if extension.upper() in file_extensions:
                    move_file_to_dir(item,  dir_name)
                else:
                    MISSING_TYPES.append(extension)
                    UNIQUE_MISSING_TYPES = list(set(MISSING_TYPES))

    if len(UNIQUE_MISSING_TYPES):
        LOGS = 'Logs'
        LOG_FILE_PATH = join(LOGS, "organize.txt")
        create_directory(LOGS)

        ALREADY_LOGGED = []
        EXTENSIONS_NOT_LOGGED = []

        if exists(LOG_FILE_PATH):
            f = open(LOG_FILE_PATH, "r")
            ALREADY_LOGGED = f.read().split("\n")
            EXTENSIONS_NOT_LOGGED = list(
                set(UNIQUE_MISSING_TYPES) - set(ALREADY_LOGGED))

        with open(LOG_FILE_PATH, "a") as f:
            for missing_type in EXTENSIONS_NOT_LOGGED:
                f.write(missing_type + "\n")
