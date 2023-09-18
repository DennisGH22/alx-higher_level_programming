import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -2, 4, -5]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 3.1]), 3.1)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4])


if __name__ == '__main__':
    unittest.main()
