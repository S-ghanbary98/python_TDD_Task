
import unittest
import pytest
from cases import Cases


class test(unittest.TestCase):
    calc = Cases()

    def test_divisible(self):
        self.assertEqual(self.calc.divisible(3,3), True)


    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

    def test_positive(self):
        self.assertEqual(self.calc.positive(7, 3), True)

