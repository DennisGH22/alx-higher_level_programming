import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):

    def test_init_with_valid_attributes(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_init_with_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3)

    def test_init_with_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3)

    def test_init_with_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_init_with_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(2, 3, 2, 1)
        expected_output = "\n  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_update_with_args(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 8, 6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_update_with_kwargs(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(width=8, height=6, x=2, y=4, id=2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
