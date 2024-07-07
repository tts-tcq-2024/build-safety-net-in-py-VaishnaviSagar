import unittest
from Soundex import generate_soundex
 
class TestSoundex(unittest.TestCase):
    def test_empty_name(self):
        self.assertEqual(generate_soundex(""), "")
    def test_single_letter_name(self):
        self.assertEqual(generate_soundex("A"), "A000")
    def test_name_with_vowels(self):
        self.assertEqual(generate_soundex("Aely"), "A400")
    def test_name_with_duplicates(self):
        self.assertEqual(generate_soundex("Aardvark"), "A636")
    def test_name_with_non_coded_letters(self):
        self.assertEqual(generate_soundex("Chae"), "C000")
    def test_name_with_multiple_codes(self):
        self.assertEqual(generate_soundex("Bhaier"), "B600")
    def test_name_with_max_length(self):
        self.assertEqual(generate_soundex("Chaeallgood"), "C420")
 
if __name__ == '__main__':
    unittest.main()
