import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 10), 15)

if __name__ == '__main__':
    unittest.main()