import unittest
from core import mobile_number_lookup

class TestCore(unittest.TestCase):
    def test_mobile_number_lookup(self):
        result = mobile_number_lookup("14158586273")
        self.assertIsNotNone(result)
        self.assertIn("valid", result)

if __name__ == "__main__":
    unittest.main()
