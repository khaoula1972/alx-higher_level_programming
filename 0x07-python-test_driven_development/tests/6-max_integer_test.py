#!/usr/bin/python3
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class: TestMaxInteger to test the max integer function
    """

    def test_empty_list(self):
        """
        Method that checks if empty list is handled
        """
        self.assertIsNone(max_integer([]))
        
    def test_positive(self):
        """
        Method that checks if positive numbers are handeled
        """
        self.assertEqual(max_integer([50, 85, 0, 9]), 85)

    def test_negative(self):
        """
        Method that checks if negative numbers are handeled
        """
        self.assertEqual(max_integer([-8, -18, -5, -6, -5, -1]), -1)

    def test_mixed(self):
        """
        Method that checks if numbers mixed are handeled
        """
        self.assertEqual(max_integer([-8, -18, 5, 0, 9]), 9)

    def test_duplicated(self):
        """
        Method that checks if duplicated numbers are handeled
        """
        self.assertEqual(max_integer([1, 1, 1, 0, 0, 8, 8, 1, 1, 1]), 8)

    def test_single(self):
        """
        Method that checks if single number is handeld
        """
        self.assertEqual(max_integer([1]), 1)

    def test_big(self):
        """
        Method that checks if long lists are handeled
        """
        self.assertEqual(max_integer([1200, 800, 990,
            600, 1540, 1200, 588, 2266, 2584, 1235, 900,
            1200, 800, 905, 800, 12000, 5884, 5668, 800,
            254, 488, 6524, 568, 5584, 54425, 487,]), 54425)

    def test_loop(self):
        """
        Method that checks if loop lists are handeled
        """
        self.assertEqual(max_integer([x**2 for x in range (10)]), 81)

    def test_operated(self):
        """
        Method that checks if operated lists are handeled
        """
        self.assertEqual(max_integer([5 - 3, 58 * 2, 5 / 2, 6 * 7, 9 + 1]), 116)
