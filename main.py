"""
Folder organizer
-----------
This script moves files to folders based on their file suffix.
"""

import shutil
import sys
from os import chdir, listdir
from os.path import isfile, join
from pathlib import Path
from typing import Set

from constants import FILE_TYPES


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    chdir(dir_path)

    unsupported_suffixes: Set[str] = set()
    files = [Path(f) for f in listdir(".") if isfile(f)]

    # Map file suffixes to their target directories
    suffix_to_dir = {
        suffix: dir_name
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
            unsupported_suffixes.add(file.suffix)

    if unsupported_suffixes:
        log_file = Path("logs/organize.txt")
        log_file.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file, "a", encoding="utf-8") as f:
            for suffix in unsupported_suffixes:
                f.write(suffix + "\n")


if __name__ == "__main__":
    main()
