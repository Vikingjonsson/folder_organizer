"""
Folder organizer
-----------
This script will move files to folders based on the file suffix.
"""

import os
import sys
import shutil

from pathlib import Path
from typing import Set, List, Dict
from constants import FILE_TYPES

if __name__ == '__main__':
    directory_path: str = sys.argv[1]

    if not directory_path:
        sys.exit()

    os.chdir(directory_path)

    unsupported_file_types: Set[str] = set()

    all_files: List[Path] = [Path(f) for f in os.listdir(
        directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Create a reverse mapping of file extensions to directory names
    extension_to_dir: Dict[str, str] = {}
    for dir_name, file_extensions in FILE_TYPES.items():
        for extension in file_extensions:
            extension_to_dir[f".{extension}"] = dir_name

    for file in all_files:
        if file.suffix in extension_to_dir:
            destination = Path(extension_to_dir[file.suffix]) / file.name
            shutil.move(file, destination)
        else:
            unsupported_file_types.add(file.suffix)

    if unsupported_file_types:
        log_file_path: Path = Path('logs/organize.txt')
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file_path, "a", encoding="utf-8") as f:
            for file_type in unsupported_file_types:
                f.write(file_type + "\n")
