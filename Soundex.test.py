import unittest
from Soundex import get_soundex_code, generate_soundex
 
class TestSoundex(unittest.TestCase):
    def test_get_soundex_code(self):
        """Test the get_soundex_code function"""
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('F'), '1')
        self.assertEqual(get_soundex_code('P'), '1')
        self.assertEqual(get_soundex_code('V'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('G'), '2')
        self.assertEqual(get_soundex_code('J'), '2')
        self.assertEqual(get_soundex_code('K'), '2')
        self.assertEqual(get_soundex_code('Q'), '2')
        self.assertEqual(get_soundex_code('S'), '2')
        self.assertEqual(get_soundex_code('X'), '2')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('T'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('N'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('z'), '2')
        self.assertEqual(get_soundex_code('1'), '0')
 
if __name__ == '__main__':
    unittest.main()
