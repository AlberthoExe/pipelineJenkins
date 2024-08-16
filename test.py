import unittest
from calculadora import suma, resta, div, multi

class TestSumNumbers(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

class Testresta(unittest.TestCase):
    def test_rest(self):
        self.assertEqual(resta(10, 8), 2)
        self.assertEqual(resta(9, 9), 0)
        self.assertEqual(resta(0, 0), 0)

class Testmulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multi(10, 8), 80)
        self.assertEqual(multi(9, 9), 81)
        self.assertEqual(multi(10, 0), 0)

class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(9, 9), 1)
        self.assertEqual(div(10, 1), 10)

    

if __name__ == "__main__":
    unittest.main()