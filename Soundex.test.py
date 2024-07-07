import unittest
from Soundex import generate_soundex
class TestSoundex(unittest.TestCase):
    def test_single_character(self):
        self.assertEqual(generate_soundex("V"), "00V0")
        self.assertEqual(generate_soundex("S"), "0S00")
    def test_case_insensitivity(self):
        self.assertEqual(generate_soundex("VAISHNAVI"), generate_soundex("vaiSHNavi"))
    def test_vowels(self):
        self.assertEqual(generate_soundex("Aeiou"), "I185")
    def test_consonants(self):
        self.assertEqual(generate_soundex("Bcdghjklmnpqrstvwxyz"), "V145")
if __name__ == '__main__':
    unittest.main()
