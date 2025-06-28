"""
Tests for folder organizer
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from main import main


class TestFolderOrganizer(unittest.TestCase):
    def setUp(self):
        """Set up test environment with temporary directory"""
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()

    def tearDown(self):
        """Clean up test environment"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def create_test_files(self, filenames):
        """Helper to create test files in the temp directory"""
        for filename in filenames:
            file_path = Path(self.test_dir) / filename
            file_path.write_text("test content")

    def test_organize_image_files(self):
        """Test organizing image files"""
        test_files = ["photo.jpg", "image.PNG", "graphic.gif"]
        self.create_test_files(test_files)

        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        images_dir = Path(self.test_dir) / "Images"
        self.assertTrue(images_dir.exists())
        self.assertTrue((images_dir / "photo.jpg").exists())
        self.assertTrue((images_dir / "image.PNG").exists())
        self.assertTrue((images_dir / "graphic.gif").exists())

    def test_organize_mixed_files(self):
        """Test organizing multiple file types"""
        test_files = [
            "document.pdf",
            "music.mp3",
            "video.mp4",
            "presentation.pptx",
            "data.xlsx",
        ]
        self.create_test_files(test_files)

        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        self.assertTrue((Path(self.test_dir) / "Documents" / "document.pdf").exists())
        self.assertTrue((Path(self.test_dir) / "Audio" / "music.mp3").exists())
        self.assertTrue((Path(self.test_dir) / "Video" / "video.mp4").exists())
        self.assertTrue(
            (Path(self.test_dir) / "Presentations" / "presentation.pptx").exists()
        )
        self.assertTrue((Path(self.test_dir) / "Spreadsheets" / "data.xlsx").exists())

    def test_case_insensitive_extensions(self):
        """Test that file extensions are handled case-insensitively"""
        test_files = ["photo.JPG", "music.MP3", "document.PDF"]
        self.create_test_files(test_files)

        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        self.assertTrue((Path(self.test_dir) / "Images" / "photo.JPG").exists())
        self.assertTrue((Path(self.test_dir) / "Audio" / "music.MP3").exists())
        self.assertTrue((Path(self.test_dir) / "Documents" / "document.PDF").exists())

    def test_unsupported_file_types(self):
        """Test logging of unsupported file types"""
        test_files = ["unknown.xyz", "mystery.abc"]
        self.create_test_files(test_files)

        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        log_file = Path(self.test_dir) / "logs" / "organize.txt"
        self.assertTrue(log_file.exists())

        log_content = log_file.read_text()
        self.assertIn(".abc", log_content)
        self.assertIn(".xyz", log_content)

    def test_no_files_to_organize(self):
        """Test behavior when directory has no files"""
        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        subdirs = [d for d in Path(self.test_dir).iterdir() if d.is_dir()]
        self.assertEqual(len(subdirs), 0)

    def test_missing_directory_argument(self):
        """Test error handling when no directory is provided"""
        with patch.object(sys, "argv", ["main.py"]):
            with self.assertRaises(SystemExit):
                main()

    def test_files_without_extensions(self):
        """Test handling of files without extensions"""
        test_files = ["README", "Makefile", "LICENSE"]
        self.create_test_files(test_files)

        with patch.object(sys, "argv", ["main.py", self.test_dir]):
            main()

        for filename in test_files:
            self.assertTrue((Path(self.test_dir) / filename).exists())

        log_file = Path(self.test_dir) / "logs" / "organize.txt"
        if log_file.exists():
            log_content = log_file.read_text()
            self.assertIn("", log_content)


if __name__ == "__main__":
    unittest.main()
