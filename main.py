"""
Folder organizer
-----------
This script will move files to folders based on the file suffix.
"""

import sys
import shutil

from os import chdir, listdir
from os.path import isfile, join
from pathlib import Path

from constants import FILE_TYPES

if __name__ == '__main__':
    dir_path: str = sys.argv[1]

    if not dir_path:
        sys.exit()

    chdir(dir_path)

    unsupported_files: set[str] = set()

    # Select all files in directory
    files = [Path(f) for f in listdir(dir_path) if isfile(join(dir_path, f))]

    # Create a reverse mapping of file suffixes to directory names
    suffix_to_dir: dict[str, str] = {}
    for dir_name, file_suffixes in FILE_TYPES.items():
        for suffix in file_suffixes:
            suffix_to_dir[suffix] = dir_name

    for file in files:
        if file.suffix in suffix_to_dir:
            destination = Path(suffix_to_dir[file.suffix]) / file.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(file, destination)
        else:
            unsupported_files.add(file.suffix)

    if unsupported_files:
        log_file_path: Path = Path('logs/organize.txt')
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file_path, "a", encoding="utf-8") as f:
            for file_type in unsupported_files:
                f.write(file_type + "\n")
