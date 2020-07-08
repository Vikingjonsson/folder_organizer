import unittest
from unittest.mock import patch
import folder_organizer


class Test_folder_organizer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_file_extension(self):
        """
        Test that it can get the file extension
        """
        result = folder_organizer.get_file_extension('item.mov')
        self.assertEqual(result, '.mov')

    def test_has_file_extension(self):
        """
        Test that a file has a file extension
        """
        result = folder_organizer.has_file_extension('item.mov')
        self.assertTrue(result)

    @patch('os.makedirs')
    def test_create_directory(self, mock_makedirs):
        """
        Test that it is possible to create a folder
        """
        folder_organizer.create_directory('test')
        mock_makedirs.assert_called_once_with('test')

    @patch('os.makedirs')
    @patch('os.path.join')
    @patch('shutil.move')
    def test_move_file_to_dir(self, mock_move, mock_path_join, mock_makedirs):
        """
        Test that file is moved into folder
        """
        folder_organizer.move_file_to_dir('file', 'directory')
        mock_path_join.assert_called()
        mock_move.assert_called()
        mock_makedirs.assert_called()


if __name__ == '__main__':
    unittest.main()
