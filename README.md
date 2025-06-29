# Folder Organizer 📁

A Python tool that automatically organizes files in a directory by moving them into folders based on their file extensions. Perfect for cleaning up Downloads folders, project directories, or any messy folder structure.

## Features

- **Automatic file organization** - Sorts files into appropriate folders based on file type
- **Case-insensitive matching** - Handles both `.jpg` and `.JPG` extensions
- **Comprehensive file type support** - Supports 10+ categories including Images, Documents, Audio, Video, Code, and more
- **Logging** - Tracks unsupported file types in `logs/organize.txt`
- **Safe operation** - Creates directories as needed, preserves original filenames

## Supported File Types

| Category | Extensions |
|----------|------------|
| **Audio** | `.aac`, `.aax`, `.flac`, `.m4a`, `.mp3`, `.ogg`, `.wav`, `.wma` |
| **Documents** | `.doc`, `.docx`, `.odt`, `.rtf`, `.tex`, `.txt`, `.wpd`, `.pdf` |
| **E-books** | `.azw`, `.azw3`, `.epub`, `.mobi` |
| **Fonts** | `.fnt`, `.fon`, `.otf`, `.ttf`, `.woff`, `.woff2` |
| **Images** | `.ai`, `.bmp`, `.gif`, `.heic`, `.ico`, `.icns`, `.jpeg`, `.jpg`, `.png`, `.ps`, `.psd`, `.svg`, `.tif`, `.tiff`, `.webp` |
| **Packages** | `.7z`, `.app`, `.dmg`, `.rar`, `.tar`, `.zip` |
| **Presentations** | `.key`, `.odp`, `.pps`, `.ppt`, `.pptx` |
| **Spreadsheets** | `.csv`, `.ods`, `.xls`, `.xlsm`, `.xlsx` |
| **System** | `.bak`, `.cab`, `.cfg`, `.cpl`, `.cur`, `.dmp`, `.drv`, `.ini`, `.lnk`, `.msi`, `.sys`, `.tmp` |
| **Video** | `.3g2`, `.avi`, `.flv`, `.h264`, `.m4v`, `.mkv`, `.mov`, `.mp4`, `.mpg`, `.mpeg`, `.rm`, `.swf`, `.vob`, `.webm`, `.wmv` |

## Usage

### Basic Usage

```bash
python main.py /path/to/folder/to/organize
```

### Example

```bash
# Organize your Downloads folder
python main.py ~/Downloads

# Organize a project directory
python main.py /Users/username/Desktop/messy-folder
```

### What happens:
1. The script scans the specified directory for files
2. Creates folders for each file type (Images, Documents, etc.)
3. Moves files to their appropriate folders
4. Logs any unsupported file extensions to `logs/organize.txt`

## Requirements

- **Python 3.9+** (uses modern type hints)
- **No external dependencies** - Uses only Python standard library

## Development

### Running Tests

```bash
python -m unittest test_main.py -v
```

### Type Checking

Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

Run type checking:
```bash
mypy main.py constants.py
```
