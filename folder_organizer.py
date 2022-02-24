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


def log_none_supported_extension(unique_missing_types):
    LOGS = 'Logs'
    LOG_FILE_PATH = join(LOGS, "organize.txt")

    if len(unique_missing_types):
        create_directory(LOGS)
        already_logged = []
        extensions_not_logged = []

        if exists(LOG_FILE_PATH):
            f = open(LOG_FILE_PATH, "r")
            already_logged = f.read().split("\n")
            extensions_not_logged = list(
                set(unique_missing_types) - set(already_logged))

    with open(LOG_FILE_PATH, "a") as f:
        for missing_type in extensions_not_logged:
            f.write(missing_type + "\n")


if __name__ == '__main__':
    print(sys.argv)
    DIRECTORY_PATH = sys.argv[1]

    if not DIRECTORY_PATH:
        exit

    chdir(DIRECTORY_PATH)

    missing_types = []
    unique_missing_types = []

    ALL_FILES_IN_DIRECTORY = [f for f in listdir(
        DIRECTORY_PATH) if isfile(join(DIRECTORY_PATH, f))]

    for item in ALL_FILES_IN_DIRECTORY:
        if has_file_extension(item):
            extension = get_file_extension(item)

            for dir_name, file_extensions in FILE_TYPES.items():
                if extension.upper() in file_extensions:
                    move_file_to_dir(item,  dir_name)
                else:
                    missing_types.append(extension)
                    unique_missing_types = list(set(missing_types))

    log_none_supported_extension(unique_missing_types)
