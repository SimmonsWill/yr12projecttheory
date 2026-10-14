import unittest
from test import valid_username

class UsernameTests(unittest.TestCase):
    def test_valid_name(self):
        self.assertTrue(valid_username("Liam2"));
        self.assertFalse(valid_username("4owen"));
        self.assertFalse(valid_username("123"));

    def test_too_short(self):
        self.assertTrue(valid_username("a"));
        self.assertFalse(valid_username("jo"));
        self.assertFalse(valid_username("2"));

    def test_too_long(self):
        self.assertTrue(valid_username("qwertyuiopas"));
        self.assertFalse(valid_username("skibididididididididididididdididididdidid"));
        self.assertFalse(valid_username("williscool123454566788900"));

if __name__ == "__main__":
    unittest.main()
