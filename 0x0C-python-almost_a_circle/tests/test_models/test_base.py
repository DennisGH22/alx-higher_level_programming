import unittest
import os
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):

    def setUp(self):
        # Create a unique temporary directory for each test case
        self.temp_dir = self.get_temp_dir()
        os.makedirs(self.temp_dir)

    def tearDown(self):
        # Remove the temporary directory and its contents
        os.rmdir(self.temp_dir)

    def get_temp_dir(self):
        # Create a unique temporary directory using the test method name
        return f"temp_test_dir_{self._testMethodName}"

    def test_init_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        dictionary_list = [{'key1': 'value1'}, {'key2': 'value2'}]
        json_string = Base.to_json_string(dictionary_list)
        self.assertEqual(json_string, '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_save_to_file(self):
        with patch('builtins.open', create=True) as mock_open:
            obj1 = Base(1)
            obj2 = Base(2)
            Base.save_to_file([obj1, obj2])

            mock_open.assert_called_once_with('Base.json', 'w', encoding='utf-8')
            handle = mock_open.return_value.__enter__.return_value
            handle.write.assert_called_once_with('[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        json_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        dictionary_list = Base.from_json_string(json_string)
        self.assertEqual(dictionary_list, [{'key1': 'value1'}, {'key2': 'value2'}])

    def test_create_rectangle(self):
        obj_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        obj = Base.create(Rectangle, **obj_dict)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_create_square(self):
        obj_dict = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        obj = Base.create(Square, **obj_dict)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_load_from_file(self):
        # Create a temporary JSON file with data
        with open(os.path.join(self.temp_dir, 'Base.json'), 'w', encoding='utf-8') as file:
            file.write('[{"id": 1}, {"id": 2}]')

        objs = Base.load_from_file()
        self.assertEqual(len(objs), 2)
        self.assertEqual(objs[0].id, 1)
        self.assertEqual(objs[1].id, 2)

    def test_save_to_file_csv(self):
        with patch('builtins.open', create=True) as mock_open:
            obj1 = Rectangle(1, 2, 3, 4, 5)
            obj2 = Rectangle(6, 7, 8, 9, 10)
            Rectangle.save_to_file_csv([obj1, obj2])

            mock_open.assert_called_once_with('Rectangle.csv', 'w', newline='')
            handle = mock_open.return_value.__enter__.return_value
            handle.write.assert_called_once_with('5,1,2,3,4\n10,6,7,8,9\n')

    def test_load_from_file_csv(self):
        # Create a temporary CSV file with data
        with open(os.path.join(self.temp_dir, 'Rectangle.csv'), 'w', newline='') as file:
            file.write('5,1,2,3,4\n10,6,7,8,9\n')

        objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(objs), 2)
        self.assertEqual(objs[0].id, 5)
        self.assertEqual(objs[0].width, 1)
        self.assertEqual(objs[0].height, 2)
        self.assertEqual(objs[0].x, 3)
        self.assertEqual(objs[0].y, 4)
        self.assertEqual(objs[1].id, 10)
        self.assertEqual(objs[1].width, 6)
        self.assertEqual(objs[1].height, 7)
        self.assertEqual(objs[1].x, 8)
        self.assertEqual(objs[1].y, 9)

if __name__ == '__main__':
    unittest.main()
