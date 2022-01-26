import unittest

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual("Hello world".split(), ["Hello","world"])

if __name__ == "__main__":
    unittest.main()