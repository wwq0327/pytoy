import unittest
import add_test

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.sum = add_test.add(3,4)

    def test_eq(self):
        self.assertEqual(self.sum, 7)

    def test_eq_not(self):
        self.assertEqual(self.sum, 5)


if __name__ == "__main__":
    unittest.main()
