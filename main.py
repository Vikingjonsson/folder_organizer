"""
Folder organizer
-----------
This script moves files to folders based on their file suffix.
"""

import shutil
import sys
from os import chdir, listdir
from os.path import isfile
from pathlib import Path

from constants import FILE_TYPES


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    chdir(dir_path)

    unsupported_suffixes: set[str] = set()
    files = [Path(f) for f in listdir(".") if isfile(f)]

    suffix_to_dir = {
        suffix.lower(): dir_name
        for dir_name, suffixes in FILE_TYPES.items()
        for suffix in suffixes
    }

    for file in files:
        file_suffix = file.suffix.lower()
        target_dir = suffix_to_dir.get(file_suffix)

        if target_dir:
            destination = Path(target_dir) / file.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(destination))
        else:
            unsupported_suffixes.add(file_suffix)

    if unsupported_suffixes:
        log_file = Path("logs/organize.txt")
        log_file.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file, "a", encoding="utf-8") as f:
            for suffix in sorted(unsupported_suffixes):
                f.write(f"{suffix}\n")


if __name__ == "__main__":
    main()
